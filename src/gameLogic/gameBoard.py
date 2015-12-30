# gameBoard.py
# ###################

import shipIds as ids
import shipOrientations as orient

# opponent board hole states
TGT_BLANK = -1
TGT_MISS = 0
TGT_HIT = 1

# board dimensions
X_LEN = 10
Y_LEN = 10
MAX_X_IDX = X_LEN - 1
MAX_Y_IDX = Y_LEN - 1

class gameBoard(object):
	"""The game board for PyBattle"""

	def __init__(self):
		# init game board
		self.self_board = gameBoard._init_matrix(None, X_LEN, Y_LEN)
		self.target_board = gameBoard._init_matrix(TGT_BLANK, X_LEN, Y_LEN)
	
	# returns false if unable to place a ship, true if successful.
	# the ship should be set with the desired position and orientation
	def tryPlaceShip(self, ship):

		if _isShipWithinBounds(ship):
			# check for conflicts with other ships
			if not _doesShipConflictWithExisting(ship):
				# no conflict - place it!
				for pos in ship.getHoleCoords():
					self.self_board[pos[0]][pos[1]] = ship 	# set pointer to ship
				return True
		# if we get here, we were unable to place the ship in the 
		# desired location
		return False

	# returns false if not a hit on self, otherwise returns
	# the shipId of the ship that was hit
	def isSelfHit(self, pos):

		# get a handle to the ship at this position
		ship = self.self_board[pos[0]][pos[1]]

		if ship == None:
			return False 	# no ship is here
		else:
			ship.recordHoleHit(pos)		# record a hit at this location
			
			# check for a ship sinking event
			if ship.state == SHIP_SUNK:
				pass	# todo: notify of ship sinking!!

			# return id of ship hit
			return ship.shipId

	# records a hit on the opponents board
	def recordTargetHit(self, pos):
		self.target_board[pos[0]][pos[1]] = TGT_HIT

	# records a miss on the opponents board
	def recordTargetMiss(self, pos):
		self.target_board[pos[0]][pos[1]] = TGT_MISS

	# initializes a matrix of x_len by y_len with
	# cells initialized to init_value
	@staticmethod
	def _init_matrix(init_value, x_len, y_len):
		return [[init_value for i in range(x_len)] for j in range(y_len)]

	# returns true if ship is within bounds of the board
	def _isShipWithinBounds(self, ship):

		# check x index
		if ship.xPos >= 0 and ship.xPos < X_LEN:
			if ship.yPos >= 0 and ship.yPos < Y_LEN:
				return true

		# if we get here, the x or y index was out of bounds!
		return false

	# returns true if ship conflicts with an existing ship
	# location
	def _doesShipConflictWithExisting(self, ship):
		# for each hole this ship covers, check
		# the existence of another ship
		for pos in ship.getHoleCoords():
			if self.self_board[pos[0]][pos[1]] != None:
				# there is a ship here!
				return True
		# if we get here, there were no conflicts
		return False
		