import paho.mqtt.client as mqtt

# Define the MQTT broker's address and port
broker_address = "localhost"
broker_port = 1883

# Create a client instance
client = mqtt.Client("publisher")

# Connect to the broker
client.connect(broker_address, broker_port)

# Publish a message to the topic "test"
client.publish("test", "Hello! This is a test message!")

# Disconnect from the broker
client.disconnect()