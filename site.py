#!/usr/bin/env python
import pika 
import sys
import json
import time

class site():
	"""Classe définissant les sites est caractérisé par :
	-Une queue 
	-Un exchange
	-Un consumer 
	-Un publisher"""
	def __init__(self,site_id,site_number):
		if type(site_id) is str: 
			site_id=int(site_id)
		if type(site_number) is str:
			site_number=int(site_number)
		
	def start_consumer():

	def start_publisher():



if __name__='__main__':

