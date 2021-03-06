#!/usr/bin/env python
import pika
import time

credentials = pika.PlainCredentials('myuser', 'mypass')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=5672,credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
