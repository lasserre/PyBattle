# clientGameEngine.py
# #####################

from gameEngine import *

class clientGameEngine(gameEngine):
	
	def __init__(self, graphicsEngine,gameConnection,p1, p2):

		# call base constructor
		super(clientGameEngine, self).__init__(graphicsEngine,gameConnection,p1, p2)

	def _beginPlaceShips(self):
		# wait for "place ships" command from server
		while len(self._gameConnection.recv_buff) <= 0:pass

		command = self._gameConnection.get_most_recent()
		if command != "Place":
			return

	def _endPlaceShips(self):
		# tell server I'm done (send ship locations...)
		self._gameConnection.send_message("done")
		pass

	def _setLocalPlayer(self):
		self._localPlayer = self._p2