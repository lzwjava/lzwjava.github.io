import os
import subprocess
import time
import shutil
import logging
import requests
import threading
import json
import urllib.parse

def setup_logging():
    """Configures basic logging for the script. Clears previous log."""
    if os.path.exists("clash.log"):
        with open("clash.log", "w"):  # clears the log file
            pass
    logging.basicConfig(
        filename="clash.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


# --- Proxy Management Functions ---


def start_system_proxy(global_proxy_address):
    """Sets system-wide proxy environment variables."""
    os.environ["GLOBAL_PROXY"] = (
        global_proxy_address  # Set for consistency if needed elsewhere
    )
    os.environ["HTTP_PROXY"] = f"http://{global_proxy_address}"
    os.environ["HTTPS_PROXY"] = f"http://{global_proxy_address}"
    os.environ["http_proxy"] = f"http://{global_proxy_address}"
    os.environ["https_proxy"] = f"http://{global_proxy_address}"
    # These typically don't need to be explicitly set to "false" with modern tools,
    # but keeping for compatibility with your original script's intent.
    os.environ["HTTP_PROXY_REQUEST_FULLURI"] = "false"
    os.environ["HTTPS_PROXY_REQUEST_FULLURI"] = "false"
    os.environ["ALL_PROXY"] = os.environ["http_proxy"]
    logging.info(f"System-wide proxy set to: {global_proxy_address}")


def stop_system_proxy():
    """Clears system-wide proxy environment variables."""
    os.environ["http_proxy"] = ""
    os.environ["HTTP_PROXY"] = ""
    os.environ["https_proxy"] = ""
    os.environ["HTTPS_PROXY"] = ""
    os.environ["HTTP_PROXY_REQUEST_FULLURI"] = "true"  # Revert to default
    os.environ["HTTPS_PROXY_REQUEST_FULLURI"] = "true"
    os.environ["ALL_PROXY"] = ""
    logging.info("System-wide proxy stopped (environment variables cleared).")


def switch_clash_proxy_group(controller_host, controller_port, group_name, proxy_name):
    """
    Switches the active proxy in a specified Clash proxy group to a new proxy.
    Returns: True if successful, False otherwise
    """
    api_base_url = f"http://{controller_host}:{controller_port}"
    encoded_group_name = urllib.parse.quote(group_name)
    url = f"{api_base_url}/proxies/{encoded_group_name}"
    headers = {"Content-Type": "application/json"}
    payload = {"name": proxy_name}

    try:
        response = requests.put(
            url, headers=headers, data=json.dumps(payload), timeout=5
        )
        response.raise_for_status()
        logging.info(f"Successfully switched '{group_name}' to '{proxy_name}'.")
        return True
    except requests.exceptions.ConnectionError:
        logging.error(
            f"Error: Could not connect to Clash API at {api_base_url} to switch proxy."
        )
        logging.error(
            "Ensure Clash is running and its external-controller is configured."
        )
        return False
    except requests.exceptions.Timeout:
        logging.error(
            f"Error: Connection to Clash API timed out while switching proxy for '{group_name}'."
        )
        return False
    except requests.exceptions.RequestException as e:
        logging.error(
            f"An unexpected error occurred while switching proxy for '{group_name}': {e}"
        )
        return False


# --- Utility Functions ---

def log_clash_output(pipe, level=logging.INFO):
    """Log output from clash process"""
    for line in iter(pipe.readline, b""):
        try:
            logging.log(level, f"[Clash] {line.decode(errors='replace').rstrip()}")
        except Exception as e:
            logging.error(f"Error decoding clash output: {e}")
    pipe.close()


def download_config(config_url, destination_path):
    """Download clash configuration from URL"""
    try:
        subprocess.run(
            ["wget", config_url, "-O", "temp_config.yaml"],
            check=True,
            capture_output=True,
        )
        
        # Ensure destination directory exists
        config_dir = os.path.dirname(destination_path)
        if config_dir:
            os.makedirs(config_dir, exist_ok=True)
        
        shutil.move("temp_config.yaml", destination_path)
        return True
    except subprocess.CalledProcessError as e:
        logging.error(
            f"Failed to download config file: {e.stderr.decode().strip() if e.stderr else str(e)}"
        )
        return False
    except Exception as e:
        logging.error(f"Error downloading config: {e}")
        return False


def start_clash_process(executable_path, host="127.0.0.1"):
    """Start the clash process and return the process handle"""
    try:
        process = subprocess.Popen(
            [executable_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        
        # Start threads to capture stdout and stderr
        threading.Thread(
            target=log_clash_output,
            args=(process.stdout, logging.INFO),
            daemon=True,
        ).start()
        threading.Thread(
            target=log_clash_output,
            args=(process.stderr, logging.ERROR),
            daemon=True,
        ).start()
        
        return process
    except Exception as e:
        logging.error(f"Failed to start Clash: {e}")
        return None


def stop_clash_process(process):
    """Stop the clash process gracefully"""
    if not process:
        return
    
    try:
        logging.info(f"Terminating Clash process (PID: {process.pid})")
        process.terminate()
        try:
            process.wait(timeout=10)
            logging.info("Clash stopped successfully.")
        except subprocess.TimeoutExpired:
            logging.warning("Clash did not terminate gracefully, killing process.")
            process.kill()
            process.wait()
    except Exception as e:
        logging.error(f"Error stopping Clash process: {e}")