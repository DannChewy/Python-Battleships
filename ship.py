
############
# SHIP CLASS - set coords and direction of each ship
############
import tile
from tile import Tile

import constants
from constants import * 

class Ship():
	def __init__(self, name, length):
			super().__init__()
			self.name = name
			self.length = length
			self.coordinates = [None] * length

	def setCoords(self,row,col):
		self.row = row
		self.col = col
		for i in range(self.length):
			if(self.direction == DIR_HORIZONTAL):
				print("Self.Coords:",self.coordinates[i])
				self.coordinates[i] = Tile(self.row,self.col + i)
			else:
				self.coordinates[i] = Tile(self.row + i, self.col)

	def setDirection(self,direction):
		self.direction = direction;
		
	def isDestroyed(self):
		for i in range(self.length):
			if(self.coordinates[i].state == TILE_STATUS_SHIP_ALIVE):
				return False
		return True

	def updateBoardState(self, board):
		for i in range(self.length):
			if not(self.coordinates[i] == None):
			 		board.changeTileState(self.coordinates[i].row ,self.coordinates[i].col, "X")   
		