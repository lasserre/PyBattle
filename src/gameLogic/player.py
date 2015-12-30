# player.py
# #################
# Represents a pyBattle player

class player(object):

	def __init__(self, name, playerId):
		self.name = name
		self.id = playerId

	# prompts the player to place the ship with the
	# given ship id. This function must return the
	# placed ship object (with position and orientation 
	# set properly)
	def placeShip(self, shipId, gameBoard):
		pass

	# prompts the player to call his next shot.
	# This function must return a (xPos, yPos) tuple
	# with the position of the next shot.
	def callShot(self, gameEngine):
		pass