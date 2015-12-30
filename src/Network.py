#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

class NetworkManager:
	PORT = 33333
	ip = ''

	def __init__(self):
		self.port = self.PORT
		self.socket = None
		#self.ip = ip
		pass

	def listen_for_connections(self):
		self.socket = socket.socket()         # Create a socket object
		host = socket.gethostname() # Get local machine name
		self.ip = socket.gethostbyname(host)

		self.socket.bind((host, self.port))        # Bind to the port
		self.print_network_info()
		self.write_to_socket()
		self.socket.listen(5)                 # Now wait for client connection.
		while True:
		   c, addr = self.socket.accept()     # Establish connection with client.
		   print 'Got connection from', addr
		   c.send('Thank you for connecting')
		   c.close()                # Close the connection


	def print_network_info(self):
		print "Server IP: " + self.ip

	def write_to_socket(self):
		print self.socket



def main():

	manager = NetworkManager()
	manager.listen_for_connections()

if __name__ == '__main__':
	main()