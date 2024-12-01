import paho.mqtt.client as mqtt
from tqdm import tqdm
import sys

def parse_parameters():
    # Default settings
    port = 1883
    keepAlive = 90

    # Parse command-line arguments
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == '-p' and i + 1 < len(sys.argv):
            port = int(sys.argv[i + 1])
        elif sys.argv[i] == '-k' and i + 1 < len(sys.argv):
            keepAlive = int(sys.argv[i + 1])
        elif sys.argv[i] == '--help' or sys.argv[i] == '-h':
            print('''\nUsage:

    python3 MQTT_SlowDoS.py -p <Broker_Port> -k <Keep_Alive>

    -p
        Port of MQTT broker (default 1883)

    -k
        Keep alive parameter of MQTT protocol (default 90 sec)
            ''')
            exit()

    return port, keepAlive

def analyze_connections(ip_list, port, keepAlive):
    accept_count = 0
    reject_count = 0

    print('\nAnalyzing IPs for connection status...\n')
    for ip in tqdm(ip_list):
        client = mqtt.Client(f'client_{ip}')
        try:
            client.connect(ip, port, keepAlive)
            print(f"{ip} -> Accept")
            accept_count += 1
            client.disconnect()  # Disconnect after successful connection
        except:
            print(f"{ip} -> Reject")
            reject_count += 1

    total_ips = len(ip_list)
    accept_percentage = (accept_count / total_ips) * 100 if total_ips > 0 else 0
    reject_percentage = (reject_count / total_ips) * 100 if total_ips > 0 else 0

    print(f"\nTotal IPs: {total_ips}")
    print(f"Accepted connections: {accept_count} ({accept_percentage:.2f}%)")
    print(f"Rejected connections: {reject_count} ({reject_percentage:.2f}%)")

if __name__ == '__main__':
    # Read IP addresses from ip_address.txt
    with open("/home/mehul/Coding/BTP/IPAddressScan/ip_addresses.txt", "r") as file:
        ip_list = [line.strip() for line in file if line.strip()]

    # Get parameters
    _port, _keepAlive = parse_parameters()

    # Analyze connections
    analyze_connections(ip_list, _port, _keepAlive)
