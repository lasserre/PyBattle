# serverGameEngine.py
# #####################

from gameEngine import *

class serverGameEngine(gameEngine):
	
	def __init__(self, graphicsEngine, gameConnection, p1, p2):

		# call base constructor
		super(serverGameEngine, self).__init__(graphicsEngine,gameConnection,p1, p2)

	def _beginPlaceShips(self):
		# send "place ships" command to client
		self._gameConnection.send_message("Place")
		pass

	def _endPlaceShips(self):
		# wait for client to tell me he's done
		while not self._gameConnection.recv_buff:pass
		reply =  self._gameConnection.get_most_recent()
		print reply
		# (make sure I don't "miss" him telling me...)
		pass

	def _setLocalPlayer(self):
		self._localPlayer = self._p1