import constants
from constants import * 

	
class Board():
	def __init__(self):
		super().__init__()
		tiles =  [None] * MAX_ROWS
	
	def cleanBoard(self):
		self.tiles = [None] * MAX_ROWS
		for rows in range(MAX_ROWS):
					self.tiles[rows] = [DEFAULT_BOARD_TILE] * MAX_COLS		
					
	def changeTileState(self, row, col, state):
		self.tiles[row][col] = state
	
	def drawBoard(self):
		for rows in range(MAX_ROWS):
			print("\n" * 2, end = "")
			for cols in range(MAX_COLS):
				  print("  ", self.tiles[rows][cols] , end = "")