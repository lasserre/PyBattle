# terminalGui.py
# ###################
# the terminal version of the gui

from __future__ import print_function
from string import ascii_uppercase

import sys
sys.path.append('../gameLogic')
import time
import gameBoard
from ship import *
import terminalColors as tColors
import gameSettings as pref

class terminalGui(object):

	def __init__(self):
		self._board_drawn = False

	def getScreenWidth(self):
		# vert. label col, margin, horiz. labels, between-lable margins, 
		# +1 for the 2-digit "10" label
		return 1 + pref.HORIZ_MARGIN + 10 + (9*pref.HORIZ_MARGIN) + 1

	def getScreenHeight(self):
		# 2 boards, separator line, status margins, status line, prompt line
		return 2 * self.getBoardHeight() + 1 + (2*pref.STATUS_MARGIN) + 1 + 1

	def getBoardHeight(self):
		# margins, horiz. label line, vert. label lines, between-label margins
		return (3 * pref.VERT_MARGIN) + 1 + 10 + (9 * pref.VERT_MARGIN)

	def moveCursorUpALine(self):
		print("\033[F", end="")
	
	def redrawBoard(self, gameBoard):
		
		# position cursor at top of board if board has already been drawn
		if self._board_drawn:
			for i in range(self.getScreenHeight()):
				self.moveCursorUpALine()
		else:
			self._board_drawn = True	# this is the first time

		self.drawTargetBoard(gameBoard)
		self.drawSeparator(pref.NEUTRAL_COLOR)
		self.drawSelfBoard(gameBoard)
		self.drawStatus()
		self.drawPrompt()

	def drawTargetBoard(self, board):
		self.printHeader(pref.TGT_COLOR)
		
		asciiIdx = 0

		for y in range(gameBoard.Y_LEN-1, -1, -1):
			
			line = ascii_uppercase[asciiIdx]

			for x in range(gameBoard.X_LEN):
				line += " " * pref.HORIZ_MARGIN
				tgtHole = board.target_board[x][y]

				if tgtHole == gameBoard.TGT_BLANK:
					line += pref.BLANK
				elif tgtHole == gameBoard.TGT_MISS:
					line += pref.TGT_MISS
				else:
					line += pref.TGT_HIT

			self.printLine(pref.TGT_COLOR, line)
			self.printVertMargin()
			asciiIdx += 1

	def drawSelfBoard(self, board):
		self.printHeader(pref.SELF_COLOR)

		asciiIdx = 0

		for y in range(gameBoard.Y_LEN-1, -1, -1):

			line = ascii_uppercase[asciiIdx]

			for x in range(gameBoard.X_LEN):
				line += " " * pref.HORIZ_MARGIN
				ship = board.self_board[x][y]

				if ship == None:
					line += pref.BLANK
				else:
					idx = ship.getHoleIdx((x,y))

					if ship.holes[idx] == HOLE_HIT:
						line += pref.SELF_HIT
					else:
						line += pref.SHIP

			self.printLine(pref.SELF_COLOR, line)
			self.printVertMargin()
			asciiIdx += 1

	def drawStatus(self):
		self.printStatusMargin()
		self.printLine(pref.NEUTRAL_COLOR, "STATUS GOES HERE...")
		self.printStatusMargin()

	def drawPrompt(self):
		self.printLine(pref.NEUTRAL_COLOR, "PROMPT TEXT >>>")

	def printLine(self, color, text):
		print(color + text + tColors.ENDC)

	def printHeader(self, color):
		self.printVertMargin()

		line = " " + (" " * pref.HORIZ_MARGIN)
		for i in range(1, 10):
			line += str(i) + (" " * pref.HORIZ_MARGIN)
		line += "10"

		self.printLine(color, line)
		self.printVertMargin()

	def printVertMargin(self):
		for i in range(pref.VERT_MARGIN):
			self.printLine(tColors.ENDC, "")

	def printStatusMargin(self):
		for i in range(pref.STATUS_MARGIN):
			self.printLine(tColors.ENDC, "")

	def drawSeparator(self, color):
		line = ""
		for i in range(self.getScreenWidth()):
			line += "-"

		self.printLine(color, line)

# tmp: test gui...
graphics = terminalGui()
board = gameBoard.gameBoard()
graphics.redrawBoard(board)
time.sleep(3)
graphics.redrawBoard(board)
