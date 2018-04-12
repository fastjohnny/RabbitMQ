#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('user', 'R2f9ytfGYbTK')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.254.64.69',port='5672',credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(
    exchange='test-x',
    routing_key='hello',
    body='Hello World! Delayed',
    properties=pika.BasicProperties(headers={"x-delay": 1000})
)

print(" [x] Sent 'Hello World!'")

connection.close()
