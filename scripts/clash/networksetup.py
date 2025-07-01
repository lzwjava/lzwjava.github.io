import subprocess
import argparse

def get_current_network_interface():
    try:
        result = subprocess.run(
            ["networksetup", "-listallnetworkservices"],
            capture_output=True,
            text=True,
            check=True
        )
        services = result.stdout.splitlines()
        for service in services:
            service = service.strip()
            if "Wi-Fi" in service or "USB 10/100 LAN" in service:
                # Verify if the interface is active
                status = subprocess.run(
                    ["networksetup", "-getinfo", service],
                    capture_output=True,
                    text=True,
                    check=True
                )
                if "IP address" in status.stdout and "0.0.0.0" not in status.stdout:
                    return service
        return None
    except subprocess.CalledProcessError as e:
        print(f"Error getting network interface: {e}")
        return None

def set_proxy(interface, proxy_host, proxy_port):
    try:
        subprocess.run(
            [
                "networksetup",
                "-setwebproxy",
                interface,
                proxy_host,
                str(proxy_port)
            ],
            check=True
        )
        subprocess.run(
            [
                "networksetup",
                "-setsecurewebproxy",
                interface,
                proxy_host,
                str(proxy_port)
            ],
            check=True
        )
        print(f"Successfully set HTTP and HTTPS proxies to {proxy_host}:{proxy_port} for {interface}")
    except subprocess.CalledProcessError as e:
        print(f"Error setting proxy: {e}")

def unset_proxy(interface):
    try:
        subprocess.run(
            ["networksetup", "-setwebproxystate", interface, "off"],
            check=True
        )
        subprocess.run(
            ["networksetup", "-setsecurewebproxystate", interface, "off"],
            check=True
        )
        print(f"Successfully unset HTTP and HTTPS proxies for {interface}")
    except subprocess.CalledProcessError as e:
        print(f"Error unsetting proxy: {e}")

def main():
    parser = argparse.ArgumentParser(description="Manage HTTP and HTTPS proxy settings for Wi-Fi or USB Ethernet on macOS")
    parser.add_argument(
        "action",
        choices=["set", "unset"],
        help="Action to perform: set or unset proxy"
    )
    args = parser.parse_args()

    proxy_host = "127.0.0.1"
    proxy_port = 7890

    network_interface = get_current_network_interface()

    if not network_interface:
        print("No active Wi-Fi or USB Ethernet interface found. Please ensure a network is connected.")
        return

    print(f"Found active network interface: {network_interface}")

    if args.action == "set":
        set_proxy(network_interface, proxy_host, proxy_port)
    else:
        unset_proxy(network_interface)

if __name__ == "__main__":
    main()