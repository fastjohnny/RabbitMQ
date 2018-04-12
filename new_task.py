#!/usr/bin/env python
import pika
import sys

message = ' '.join(sys.argv[1:]) or "Hello World!"

credentials = pika.PlainCredentials('myuser', 'mypass')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=5672,credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
