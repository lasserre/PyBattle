# clientGameEngine.py
# #####################

from gameEngine import *

class clientGameEngine(gameEngine):
	
	def __init__(self, p1, p2):

		# call base constructor
		super(clientGameEngine, self).__init__(graphicsEngine, p1, p2)

	def _beginPlaceShips(self):
		# wait for "place ships" command from server
		pass

	def _endPlaceShips(self):
		# tell server I'm done (send ship locations...)
		pass