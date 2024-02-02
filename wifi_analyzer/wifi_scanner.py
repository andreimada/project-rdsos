import subprocess
import re


def enable_monitor_mode(interface):
    """
    Enables monitor mode on the specified wireless interface.
    Replace 'airmon-ng start' with the appropriate command for your system, if different.
    """
    try:
        subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)
        print(f"Monitor mode enabled on {interface}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to enable monitor mode: {e}")


def scan_networks(interface):
    """
    Scans for WiFi networks using the specified interface in monitor mode.
    This example uses 'iwlist' for scanning, replace it with 'iw' or appropriate tool for your system.
    """
    try:
        result = subprocess.run(["sudo", "iwlist", interface, "scan"], capture_output=True, text=True, check=True)
        networks = parse_networks(result.stdout)
        return networks
    except subprocess.CalledProcessError as e:
        print(f"Failed to scan networks: {e}")
        return []


def parse_networks(scan_output):
    """
    Parses the output from the scanning tool to extract network details.
    This function needs to be tailored to the output format of your scanning tool.
    """
    networks = []
    for line in scan_output.split('\n'):
        if "ESSID:" in line:
            ssid = re.search(r'"(.*?)"', line).group(1)
            networks.append(ssid)
    return networks


if __name__ == "__main__":
    interface = "wlan0"
    enable_monitor_mode(interface)
    networks = scan_networks(interface)
    print("Found networks:", networks)
