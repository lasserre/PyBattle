# gameEngine.py
# ##################
# The primary game engine for pyBattle

from gameBoard import *

# role definitions
#ROLE_SERVER = 0
#ROLE_CLIENT = 1

class gameEngine(object):
	
	# graphicsEngine - the graphics engine for pyBattle
	# p1 - player 1 (by convention, the server)
	# p2 - player 2 (by convention, the client)
	def __init__(self, graphicsEngine, gameConnection, p1, p2):
		
		print "Game Created with " + p1.name + " and " + p2.name
		self._board = gameBoard()
		self._p1 = p1
		self._p2 = p2
		self._graphics = graphicsEngine
		self._gameConnection = gameConnection

	def startGame(self):

		# place ships (show "waiting on [player]...")
		self._placeShips()

		self._chooseWhoGoesFirst()

		self._playGame()



	


	# this function is called by the player with
	# a (xPos, yPos) tuple (pos) of the desired
	# shot to call. This function must be implemented
	# by the derived classes.
	def callShot(self, pos):
		pass

	# derived classes must implement
	def _beginPlaceShips(self):
		pass

	# derived classes must implement
	def _endPlaceShips(self):
		pass

	# performs the placeShips phase of game setup
	def _placeShips(self):
		
		self._beginPlaceShips()

		# place my ships...

		self._endPlaceShips()

	# derived classes must implement
	def _chooseWhoGoesFirst(self):
		pass

	#This method is the method that loops continually until the game is over
	def _playGame(self):
		while True:
			#TODO: main Turn-based game logic goes here
			pass
