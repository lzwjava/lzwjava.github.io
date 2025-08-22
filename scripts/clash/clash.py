import os
import time
import argparse
import logging

from speed import get_top_proxies
from clash_utils import (
    setup_logging,
    start_system_proxy,
    stop_system_proxy,
    switch_clash_proxy_group,
    download_config,
    start_clash_process,
    stop_clash_process
)

# --- Configuration ---
CLASH_CONTROLLER_HOST = "127.0.0.1"
CLASH_CONTROLLER_PORT = 9090
TARGET_PROXY_GROUP = "🚧Proxy"


def main():
    """Main function to manage Clash config, restart, and select best proxy."""
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Clash configuration and management script."
    )
    parser.add_argument(
        "--minutes", type=int, default=20, help="Minutes between updates (default: 20)"
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=1000,
        help="Number of iterations (default: 1000)",
    )
    parser.add_argument(
        "--config-url",
        type=str,
        default=os.getenv("CLASH_DOWNLOAD_URL"),
        help="URL to download Clash configuration from. Defaults to CLASH_DOWNLOAD_URL environment variable if set, otherwise a hardcoded URL.",
    )
    parser.add_argument(
        "--clash-executable",
        type=str,
        default=os.getenv("CLASH_EXECUTABLE"),
        help="Path to the Clash executable. Defaults to CLASH_EXECUTABLE environment variable if set.",
    )
    parser.add_argument(
        "--hk",
        action="store_true",
        help="Include HK proxies in selection (not just SG/TW)",
    )
    args = parser.parse_args()

    ITERATIONS = args.iterations
    SLEEP_SECONDS = args.minutes * 60
    config_download_url = args.config_url
    clash_executable_path = args.clash_executable

    if not config_download_url:
        logging.critical(
            "Error: No configuration download URL provided. Please set CLASH_DOWNLOAD_URL environment variable or use --config-url argument."
        )
        return  # Exit if no URL is available

    if not clash_executable_path:
        logging.critical(
            "Error: No Clash executable path provided. Please set CLASH_EXECUTABLE environment variable or use --clash-executable argument."
        )
        return  # Exit if no executable path is available

    clash_config_dir = os.path.expanduser("~/.config/clash")
    clash_config_path = os.path.join(clash_config_dir, "config.yaml")

    for i in range(1, ITERATIONS + 1):
        logging.info(f"--- Starting Iteration {i} of {ITERATIONS} ---")

        # Step 1: Stop any existing system proxy settings
        stop_system_proxy()

        # Step 2: Download and update Clash config
        clash_config_path = os.path.join(clash_config_dir, "config.yaml")
        if not download_config(config_download_url, clash_config_path):
            logging.error("Skipping to next iteration.")
            time.sleep(10)
            continue

        # Step 3: Start Clash in the background
        clash_process = start_clash_process(clash_executable_path)
        if not clash_process:
            logging.error("Skipping to next iteration.")
            time.sleep(10)
            continue

        # Step 4: Test proxy speeds and select the best one
        best_proxy_name = None
        try:
            logging.info("Testing proxy speeds to find the best one...")
            top_proxies = get_top_proxies(num_results=20)  # Get top 5 proxies
            if top_proxies:
                # Check for SG or TW in proxy names
                # Check for SG or TW in proxy names (or HK if --hk is set)
                for proxy in top_proxies:
                    proxy_name = proxy["name"]
                    if args.hk:
                        if any(x in proxy_name for x in ["HK", "SG", "TW"]):
                            best_proxy_name = proxy_name
                            logging.info(
                                f"Selected proxy '{best_proxy_name}' (contains HK/SG/TW) with latency {proxy['latency']}ms"
                            )
                            break
                    else:
                        if any(x in proxy_name for x in ["SG", "TW"]):
                            best_proxy_name = proxy_name
                            logging.info(
                                f"Selected proxy '{best_proxy_name}' (contains SG/TW) with latency {proxy['latency']}ms"
                            )
                            break
                        # If no SG or TW proxy is found, use the first one
                        if not best_proxy_name:
                            best_proxy_name = top_proxies[0]["name"]
                            logging.info(
                                f"No SG or TW proxy found. Selected first proxy '{best_proxy_name}' with latency {top_proxies[0]['latency']}ms"
                            )
            else:
                logging.warning(
                    "No successful proxy tests. Cannot select a best proxy for this iteration."
                )
        except Exception as e:
            logging.error(f"Error during proxy speed testing: {e}")

        # Step 5: Switch Clash's proxy group to the best proxy (if found)
        if best_proxy_name:
            # Before setting system proxy, ensure Clash is set up correctly.
            # Set the system-wide proxy to point to Clash's local HTTP proxy.
            clash_local_proxy_address = f"{CLASH_CONTROLLER_HOST}:7890"
            start_system_proxy(clash_local_proxy_address)

            if not switch_clash_proxy_group(
                CLASH_CONTROLLER_HOST, 
                CLASH_CONTROLLER_PORT, 
                TARGET_PROXY_GROUP, 
                best_proxy_name
            ):
                logging.error(
                    f"Failed to switch Clash group '{TARGET_PROXY_GROUP}' to '{best_proxy_name}'."
                )
        else:
            logging.warning(
                "No best proxy found, skipping proxy group switch and system proxy setup for this iteration."
            )

        # Step 6: Wait for the specified duration
        logging.info(
            f"Waiting for {SLEEP_SECONDS / 60} minutes before next iteration..."
        )
        time.sleep(SLEEP_SECONDS)

        # Step 7: Stop Clash process
        stop_clash_process(clash_process)

        logging.info(f"--- Iteration {i} completed ---")

    logging.info(f"Completed {ITERATIONS} iterations. Script finished.")


if __name__ == "__main__":
    main()
