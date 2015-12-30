# gameEngine.py
# ##################
# The primary game engine for pyBattle

from gameBoard import *

class gameEngine(object):
	"""The game engine for pyBattle"""
	
	def __init__(self):
		
		self._board = gameBoard()

	def startGame(self):

		# place ships (show "waiting on [player]...")