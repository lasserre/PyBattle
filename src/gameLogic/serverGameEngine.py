# serverGameEngine.py
# #####################

from gameEngine import *

class serverGameEngine(gameEngine):
	
	def __init__(self, graphicsEngine, p1, p2):

		# call base constructor
		super(serverGameEngine, self).__init__(graphicsEngine, p1, p2)

	def _beginPlaceShips(self):
		# send "place ships" command to client
		pass

	def _endPlaceShips(self):
		# wait for client to tell me he's done
		# (make sure I don't "miss" him telling me...)
		pass