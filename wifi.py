import pywifi
from pywifi import const
import subprocess

def get_wifi_details():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Assuming only one WiFi interface is available
    iface.scan()
    wifi_list = iface.scan_results()
    details = []
    for cell in wifi_list:
        wifi_details = {
            'SSID': cell.ssid,
            'Signal Strength (dBm)': cell.signal,
            'Encryption Type': const.AUTH_ALG_NAMES[cell.akm[0]],
            'Channel': cell.channel,
            'Address': cell.bssid,
            'Frequency (MHz)': cell.frequency,
            'Mode': cell.mode
        }
        details.append(wifi_details)
    return details

def get_network_speed():
    # Use subprocess to execute the 'speedtest-cli' command line tool to measure network speed
    speed_test_output = subprocess.check_output(["speedtest-cli", "--simple"]).decode()
    speed_test_lines = speed_test_output.strip().split("\n")
    download_speed, upload_speed = speed_test_lines[0].split(":")[1].strip(), speed_test_lines[1].split(":")[1].strip()
    return {'Download Speed': download_speed, 'Upload Speed': upload_speed}

def get_network_info():
    # Use subprocess to execute system commands to retrieve network information
    ip_address = subprocess.check_output(["hostname", "-I"]).decode().strip()
    mac_address = subprocess.check_output(["cat", "/sys/class/net/wlan0/address"]).decode().strip()
    return {'IP Address': ip_address, 'MAC Address': mac_address}

if __name__ == "__main__":
    print("Searching for WiFi networks...")
    wifi_details = get_wifi_details()
    print("WiFi networks found:")
    for index, network in enumerate(wifi_details, start=1):
        print(f"Network {index}:")
        for key, value in network.items():
            print(f"{key}: {value}")
        print()

    print("Getting network speed...")
    speed_details = get_network_speed()
    for key, value in speed_details.items():
        print(f"{key}: {value}")

    print("Getting network info...")
    network_info = get_network_info()
    for key, value in network_info.items():
        print(f"{key}: {value}")

