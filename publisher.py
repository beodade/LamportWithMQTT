#!/usr/bin/env python
import pika
import sys
class Publisher(Object):
	def __init__(self,exchange_name,queue_name):
		self.exchange_name=exchange_name
		self.queue_name=queue_name
		connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
		self.connection=connection
		channel = connection.channel()
		channel.exchange_declare(exchange=exchange_name,exchange_type='fanout')
		self.site_number=int(exchange_name[:1])
	def send_request(self,time):
		message = "{"+self.site_number+"}"+"{"+time+"}"
		self.channel.basic_publish(exchange=self.exchange_name,routing_key='',body=message)
	def close_connection(self):
		self.connection.close()

if __name__= main :
	if len(sys.argv) != 3
		print("Warning : python publisher.py exchange_name queue_name")
	else:
		pub=Publisher(sys.argv[1],sys.argv[2])
		try : 
			pub.send_request(0)
		except KeyboardInterrupt:
			pub.close_connection()
