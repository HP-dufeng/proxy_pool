import pika
import sys
import json

def push(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='proxy_pool_exchange',
                            type='direct')

    channel.queue_declare(queue='validate_queue')

    message = json.dumps(data)
    channel.basic_publish(exchange='proxy_pool_exchange',
                        routing_key='validate_queue',
                        body=message,
                        properties=pika.BasicProperties(
                            #  content_type='text/plain',
                        ))

    connection.close()