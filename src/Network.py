#!/usr/bin/python           

import socket               
import select
import threading
import time

class NetworkHelper:
	PORT = 33333
	ip = ''

	def __init__(self):
		self.port = self.PORT
		self.socket = None
		
	def listen_for_connections(self):
		# Create a socket object
		self.socket = socket.socket() 

	    # Get local machine name and IP    
		host = socket.gethostname() 
		self.ip = socket.gethostbyname(host)

		# Bind to the port
		self.socket.bind((host, self.port))        
		self.print_network_info()

		# Now wait for client connection.
		self.socket.listen(5)                 
		while True:
		   # Establish connection with client.
		   self.socket, addr = self.socket.accept()     
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
		ip = raw_input("Please Enter The Server IP: ")
		return ip
	# def read_from_socket(self):
	# 	recv_data = self.socket.recv(4096)
	# 	return recv_data

	def close_socket():
		self.socket.close()

	


class GameConnection:

	BUFF_SIZE = 4096

	#recv_buff = []

	def __init__(self,socket,helper):
		self.socket = socket
		self.helper = helper
		self.recv_buff = []

	def __del__(self):
		self.socket.close()

	#send_message puts data into send_buffer which is checked periodically
	def send_message(self,data):
		print "Sending: " + data
		self.socket.send(data)

	#This method listens on a different thread for incoming messages
	#and adds them to recv_buff
	def _listen_for_incoming(self):
		while True:
			message = self.socket.recv(GameConnection.BUFF_SIZE)
			if len(message) > 0:
				print "Received: " + message
				self.recv_buff.append(message)
				#time.sleep(2)

	def get_most_recent(self):
		if len(self.recv_buff) > 0:
			return self.recv_buff.pop(0)

	def run(self,isServer):
		print "Game Connection Established"
		self.isServer = isServer
		
		thread = threading.Thread(target=self._listen_for_incoming, args=())
		thread.setDaemon(True)                          
		thread.start() 

		# if not(self.isServer):
		# 	message = self.get_data_with_prompt("Please Enter Your Name: ")
		# 	self.send_message(message)
		# while True and not(self.isServer):
		# 	message = raw_input("Send a Message: ")
		# 	self.send_message(message)
		# 	if message == 'end':
		# 		print "Buffer" + self.recv_buff
		# 		self.socket.close()


		# self.socket.close()
	def get_data_with_prompt(self,prompt):
		return raw_input(prompt)
			



def main():
	usr_in = raw_input("Would to be a server(1),be a client(2)")
	manager = NetworkHelper()

	if usr_in == '1':
		cnxn = manager.listen_for_connections()
		cnxn.run(True)
		
	elif usr_in == '2':
		print "I am client"
		cnxn = manager.connect_to_server()
		cnxn.run(False)
		# usr_in = raw_input("Send a Message: ")
		# cnxn.send_message(usr_in)

if __name__ == '__main__':
	main()