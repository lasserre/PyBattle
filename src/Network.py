#!/usr/bin/python           

import socket               
import select

class NetworkHelper:
	PORT = 33333
	ip = ''

	def __init__(self):
		self.port = self.PORT
		self.socket = None
		
	def listen_for_connections(self):
		self.socket = socket.socket()         # Create a socket object
		host = socket.gethostname() # Get local machine name
		self.ip = socket.gethostbyname(host)

		self.socket.bind((host, self.port))        # Bind to the port
		self.print_network_info()
		self.socket.listen(5)                 # Now wait for client connection.
		while True:
		   self.socket, addr = self.socket.accept()     # Establish connection with client.
		   print 'Got connection from', addr
		   self.socket.send('Thank you for connecting')
		   return GameConnection(self.socket,self)

	def connect_to_server(self):
		ip = self.ask_for_server_ip()
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((ip,NetworkHelper.PORT))
		return GameConnection(self.socket,self)

	def print_network_info(self):
		print "Server IP: " + self.ip

	# def write_to_socket(self,data):
	# 	print "Sending: " + data
	# 	self.socket.send(data)

	def ask_for_server_ip(self):
		ip = raw_input("What is the server IP? ")
		return ip
	# def read_from_socket(self):
	# 	recv_data = self.socket.recv(4096)
	# 	return recv_data

	def close_socket():
		self.socket.close()

class GameConnection:

	BUFF_SIZE = 4096

	def __init__(self,socket,helper):
		self.socket = socket
		self.helper = helper

	def __del__(self):
    	#print self.id, 'died'
    	#print'destroying Game connection'
		self.socket.close()

	def send_message(self,data):
		self.socket.send(data)

	def recv_message(self):
		message = self.socket.recv(GameConnection.BUFF_SIZE)
		print "Received: " + message
		return len(message)

	def run(self,isServer):
		self.isServer = isServer
		while True:
			readable,writeable,in_error = select.select([self.socket],[self.socket],[],0)
		
			hasData = len(readable) > 0
			if hasData:
				self.recv_message()

			if len(writeable) >0 and not(self.isServer):
				message = raw_input("Send a Message: ")
				self.send_message(message)
				if message == 'end':
					self.socket.close()


		self.socket.close()
			



def main():
	usr_in = raw_input("Would to be a server(1),be a client(2)")
	manager = NetworkHelper()

	if usr_in == '1':
		cnxn = manager.listen_for_connections()
		cnxn.run(True)
		
	elif usr_in == '2':
		cnxn = manager.connect_to_server()
		cnxn.run(False)
		# usr_in = raw_input("Send a Message: ")
		# cnxn.send_message(usr_in)

if __name__ == '__main__':
	main()