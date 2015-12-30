# ship.py
# ###################

import shipIds as ids

# ship lengths
PATROL_BOAT_LEN = 2
SUBMARINE_LEN = 3
DESTROYER_LEN = 3
BATTLESHIP_LEN = 4
CARRIER_LEN = 5

# base ship class
class ship(object):

	def __init__(self, shipId, length):
		self._id = shipId
		self._length = length

	@property
	def length(self):
	    return self._length
	
	# the x-position of the ship (0-9 valid, -1 = not placed)
	@property
	def xPos(self):
	    return self._xPos

	# the y-position of the ship (0-9 valid, -1 = not placed)	
	@property
	def yPos(self):
	    return self._yPos

	# the orientation of the ship (N, S, E, or W)
	@property
	def orientation(self):
	    return self._orientation

	# the setter for the orientation
	@property
	def orientation(self, orient):
		self._orientation = orient

class patrolBoat(ship):

	def __init__(self):
		super(patrolBoat, self).__init__(ids.PATROL_BOAT, PATROL_BOAT_LEN)