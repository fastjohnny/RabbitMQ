#!/usr/bin/env python
import pika
import sys
print sys.argv[1]
arg=sys.argv[1]
credentials = pika.PlainCredentials('user', 'R2f9ytfGYbTK')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.254.64.69',port='5672',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue=arg)
