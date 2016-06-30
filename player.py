import ship
from ship import Ship

import constants
from constants import * 

class Player():
	def __init__(self, ID):
		super().__init__()
		self.player = ID

	def initialiseShips(self, board):
		self.allShips = self.createShips()
		for i in range(MAX_SHIPS):
			print("")
			acceptShipCoordinates(self.allShips[i])
			#board.placeShip(self.allShips[i])
			print("")
			board.printPlayersShips()


	def createShips(self):
		return [Ship("Destroyer",2),Ship("Submarine",3),Ship("Cruiser",3),Ship("Battleship",4),Ship("Carrier",5)]
		
	def hasLost(self):
		for i in range(MAX_SHIPS):
			if not(self.allShips[i].isDestroyed()):
				return False
		return True