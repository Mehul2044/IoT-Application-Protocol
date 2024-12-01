import pika

# Callback function to handle incoming messages
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue named 'hello'
channel.queue_declare(queue='hello')

# Register the callback function to consume messages from the 'hello' queue
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

# Start consuming messages from the 'hello' queue
print(' [*] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()