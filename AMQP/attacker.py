import pika
import time

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue named 'hello'
channel.queue_declare(queue='hello')

# Message to be sent in chunks
message = "Hello, World!"
chunk_size = 1  # Define the size of each chunk
delay = 1  # Delay in seconds between each chunk

# Split the message into chunks and send each chunk with a delay
for i in range(0, len(message), chunk_size):
    chunk = message[i:i + chunk_size]
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=chunk)
    print(f" [x] Sent chunk: '{chunk}'")
    time.sleep(delay)  # Delay before sending the next chunk

# Close the connection
connection.close()
