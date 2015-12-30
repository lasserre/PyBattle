# player.py
# #################
# Represents a pyBattle player
import time
class player(object):

	def __init__(self, name):
		self.name = name

	# prompts the player to place the ship with the
	# given ship id. This function must return the
	# placed ship object (with position and orientation 
	# set properly)
	def placeShip(self, shipId, gameBoard):
		while 1:
			print "Placing...\n"
			time.sleep(3)
		pass

	# prompts the player to call his next shot.
	# This function must return a (xPos, yPos) tuple
	# with the position of the next shot.
	def callShot(self, gameEngine):
		pass