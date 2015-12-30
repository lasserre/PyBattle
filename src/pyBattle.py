# main.py...
import sys
sys.path.append('gameLogic')	# add gameLogic to path
from gameEngine import *
from player import *
from serverGameEngine import *
from clientGameEngine import *
from Network import *

def startNewGame():
	
	engine = create_networked_game()
	engine.startGame()	# start the game

def joinGame():
	print "joining game..."

	engine = join_networked_game()
	engine.startGame()

	# cls: just need to FIND the server here...we will
	# handle game setup/synchronization in engine.startGame()

def exit():
	sys.exit()

def create_networked_game():
	serverName = raw_input("Please Enter Your Name: ")
	#create server connection and wait for client
	helper = NetworkHelper()
	gameConnection = helper.listen_for_connections()
	gameConnection.run(True)


	#wait for player info from client
	gameConnection.send_message(serverName)
	print "Waiting for player 2 name"
	
	while len(gameConnection.recv_buff) <= 0:pass

	clientName = gameConnection.get_most_recent()

	# init players/engine
	p1 = player(serverName)
	p2 = player(clientName)

	return serverGameEngine(None, gameConnection, p1, p2)

def join_networked_game():
	helper = NetworkHelper()
	gameConnection = helper.connect_to_server()
	gameConnection.run(True)

	while len(gameConnection.recv_buff) <= 0:pass

	serverName = gameConnection.get_most_recent()
	clientName = raw_input("Please Enter Your Name: ")

	gameConnection.send_message(clientName)

	p1 = player(serverName)
	p2 = player(clientName)

	return clientGameEngine(None,gameConnection,p1,p2)




# Program Constants
_menu_separator = "---------------------------"
_error_msg = "Please type the number for the action you wish to select."

# Menu Dictionary Format
#   index -> ( display text, onSelected() )
_menu = {
	1: ("Start a new game", startNewGame),
	2: ("Join an existing game", joinGame),
	3: ("Quit", lambda : exit)
}

# Returns the Game Menu as a String
def getGameMenuString():

	s = _menu_separator + "\n"
	s += "PyBattle Game Menu\n"
	s += _menu_separator + "\n"
	s += "\n"

	for k, v in _menu.iteritems():
		s += '{0}: {1}\n'.format(k, v[0])

	return s

# Runs the Game Menu. Returns 1 if invalid selection specified
def runGameMenu():

	# print menu
	print getGameMenuString()

	selStr = raw_input("Enter selection >>> ")
	sel = 0
	
	try:
		sel = int(selStr)
	except:
		print "Invalid selection '{0}'. {1}".format(selStr, _error_msg)
		return 1

	# handle selection
	if sel in _menu:
		_menu[sel][1]()
	else:
		print "No menu option '{0}'".format(sel)
		return 1

	return 0


def main():
	
	print "PyBattle - Limited Christmas Edition (c) 2015"

	while runGameMenu() == 1:
		print "\n\n"	# add some space...

	# print game menu
	# run server or client?


# run main...
main()