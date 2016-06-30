

"""
Board code?
"""
import constants
from constants import * 



import player
from player import Player
		
import board
from board import Board
		
############
# Game CLASS - responsible for update and draw of game
############
class Game():
	def __init__(self):
		 super().__init__()
		 self.shipBoard = Board()
		 self.shotBoard = Board()
		 self.playerturn = 1

	def whosturn(self):
		if (self.playerturn%2 == 1):
			return self.player1
		else:
			return self.player2	

	def changeturn(self):
		self.playerturn += 1
		#wall of blank
		clear()
		print("Player ", self.whosturn().player, "'s  turn")
		
	def printPlayersShots(self):
		print("")
		print("------------SHOTS FIRED--------------")
		self.shotBoard.cleanBoard()
		self.shotBoard.drawBoard()
							  


	def printPlayersShips(self):
		print("")
		print("---------------SHIPS-----------------")
		self.shipBoard.cleanBoard()
		currentP = self.whosturn()

		for i in range(MAX_SHIPS):
			currentP.allShips[i].updateBoardState(self.shipBoard)
		
		self.shipBoard.drawBoard()

	def initPlayers(self):
		self.player1 = Player(1)
		self.player2 = Player(2)
		print("Player 1 -- initialise your BATTLESHIPSS!!!!!")
		self.player1.initialiseShips(self)
		self.changeturn()
		print("Player 2")		
		self.player2.initialiseShips(self)			 
		self.changeturn()


	def beginGame(self):
		while not (self.player1.hasLost() or self.player2.hasLost()):
			response = input("press ENTER to being turn")
			self.printPlayersShots()
			print("")
			self.printPlayersShips()
			print("")
			response = input("where do yo want to shoot")
			print("You sunk my battleship")
			response = input("press ENTER to end turn")
			self.changeturn()





