#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('user', 'R2f9ytfGYbTK')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.254.64.69',port='5672',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.exchange_declare("test-x", "x-delayed-message", arguments={"x-delayed-type":"direct"})  

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
