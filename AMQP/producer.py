import pika

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue named 'hello'
channel.queue_declare(queue='hello')

# Send a message to the 'hello' queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello, World!')
print(" [x] Sent 'Hello, World!'")

# Close the connection
connection.close()