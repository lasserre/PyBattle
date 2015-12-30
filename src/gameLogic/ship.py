# ship.py
# ###################

import shipIds as ids
import shipOrientations as orient

# ship lengths
PATROL_BOAT_LEN = 2
SUBMARINE_LEN = 3
DESTROYER_LEN = 3
BATTLESHIP_LEN = 4
CARRIER_LEN = 5

# ship states
SHIP_ALIVE = 1
SHIP_SUNK = 0

# ship hole states
HOLE_HIT = 1
HOLE_NORMAL = 0

# base ship class
class ship(object):

	def __init__(self, shipId, length):
		self._id = shipId
		self._length = length
		self.orientation = orient.NORTH
		self.state = SHIP_ALIVE
		self.holes = [HOLE_NORMAL] * length

	# the length of the ship
	@property
	def length(self):
	    return self._length

	# the type of ship
	@property
	def shipId(self):
	    return self._id
	
	# the x-position of the ship (0-9 valid, -1 = not placed)
	@property
	def xPos(self):
	    return self._xPos

	# the y-position of the ship (0-9 valid, -1 = not placed)	
	@property
	def yPos(self):
	    return self._yPos

	def isHorizontal(self):
		return self.orientation == orient.EAST || self.orientation == orient.WEST

	def isVertical(self):
		return self.orientation == orient.NORTH || self.orientation == orient.SOUTH

	# records a hole hit at the given position, and 
	# updates state if the ship has been sunk
	def recordHoleHit(self, pos):
		idx = self.getHoleIdx(pos)
		self.holes[idx] = HOLE_HIT	# record the hit!

		hasUnhitHole = False

		for i in range(self.length):
			if self.holes[i] == HOLE_NORMAL:
				hasUnhitHole = True
				break

		# record sunk state if no unhit holes
		if not hasUnhitHole:
			self.state = SHIP_SUNK

	# gets the index of the hole at position 'pos'
	def getHoleIdx(self, pos):
		
		if self.isHorizontal():
			return abs(pos[0] - self.xPos)
		else:
			return abs(pos[1] - self.yPos)
			
    # returns a list of positions (xPos, yPos)
    # of each of the holes for this ship
	def getHoleCoords(self):

		xStart = 0
		yStart = 0

		if isHorizontal():
			# take y as-is
			yStart = self.yPos

			# take leftmost position for x
			if self.orientation == orient.EAST:
				xStart = self.xPos
			else:
				xStart = self.xPos - (self.length - 1)

		else:
			# take x as-is
			xStart = self.xPos

			# take bottom position for y
			if self.orientation == orient.NORTH:
				yStart = self.yPos
			else:
				yStart = self.yPos - (self.length - 1)

		# return a list of tuples representing the positions of the holes
		holeCoords = []

		if isHorizontal():
			# iterate over x positions...
			for x in range(xStart, xStart + self.length):
				holeCoords.append((x, yPos))
		else:
			# iterate over y positions...
			for y in range(yStart, yStart + self.length):
				holeCoords.append((xPos, y))

		return holeCoords

class patrolBoat(ship):
	def __init__(self):
		super(patrolBoat, self).__init__(ids.PATROL_BOAT, PATROL_BOAT_LEN)

class submarine(ship):
	def __init__(self):
		super(submarine, self).__init__(ids.SUBMARINE, SUBMARINE_LEN)

class destroyer(ship):
	def __init__(self):
		super(destroyer, self).__init__(ids.DESTROYER, DESTROYER_LEN)

class battleship(ship):
	def __init__(self):
		super(battleship, self).__init__(ids.BATTLESHIP, BATTLESHIP_LEN)

class carrier(ship):
	def __init__(self):
		super(carrier, self).__init__(ids.CARRIER, CARRIER_LEN)