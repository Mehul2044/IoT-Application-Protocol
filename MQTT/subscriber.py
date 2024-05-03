import paho.mqtt.client as mqtt

# Define the MQTT broker's address and port
broker_address = "localhost"
broker_port = 1883


# Callback function to handle incoming messages
def on_message(client, userdata, message):
    print("Received message on topic '{}': {}".format(message.topic, message.payload.decode()))


# Create a client instance
client = mqtt.Client("subscriber")

# Attach the callback function to the client
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, broker_port)

# Subscribe to the topic "test"
client.subscribe("test")

# Start the MQTT loop to listen for messages
client.loop_forever()
