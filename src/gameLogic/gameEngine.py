# gameEngine.py
# ##################
# The primary game engine for pyBattle

from gameBoard import *

class gameEngine(object):
	"""The game engine for pyBattle"""
	
	# p1 - player 1
	# p2 - player 2
	def __init__(self, p1, p2):
		
		self._board = gameBoard()
		self._p1 = p1
		self._p2 = p2

	def startGame(self):
		pass
		# place ships (show "waiting on [player]...")