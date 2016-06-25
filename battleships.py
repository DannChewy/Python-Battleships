"""
Board code?
"""

MAX_COLS = 10
MAX_ROWS = 10
MAX_SHIPS = 2
DIR_HORIZONTAL = 0
DIR_VERTICAL = 1

TILE_STATUS_SHIP_ALIVE = 0

#board = [None] * MAX_ROWS
class Tile():
		def __init__(self, row, col):
					 super().__init__()
					 self.row = row
					 self.col = col
					 self.state = 0
	  
############
# SHIP CLASS - set coords and direction of each ship
############
class Ship():
	def __init__(self, name, length):
			super().__init__()
			self.name = name
			self.length = length
			self.status = "alive"
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


############
# PLAYER CLASS - player and ship management
############
class Player():
	def __init__(self, ID):
		super().__init__()
		self.player = ID

	def initialiseShips(self, board):
		self.allShips = self.createShips()
		for i in range(MAX_SHIPS):
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

############
# BOARD CLASS - draws board
############
class Board():

	def __init__(self):
		 super().__init__()
		 self.board = [None] * MAX_ROWS
		 self.playerturn = 1

	def whosturn(self):
		if (self.playerturn%2 == 1):
			return self.player1
		else:
			return self.player2	

	def changeturn(self):
		self.playerturn += 1
		#wall of blank
		print("\n" * 50)
		print("Player ", self.whosturn().player, "'s  turn")
		
	def printPlayersShots(self):
		print("")
		print("------------SHOTS FIRED--------------")
		shotBoard = self.getNewBoard()
		
		for rows in range(MAX_ROWS):
					print("")
					for cols in range(MAX_COLS):
							  print(shotBoard[rows][cols] , end = "")
		
		
		
	def getNewBoard(self):
		thisBoard = [None] * MAX_ROWS
		for rows in range(MAX_ROWS):
					thisBoard[rows] = [0] * MAX_COLS
		return thisBoard

	def printPlayersShips(self):
		print("")
		print("---------------SHIPS-----------------")
		self.refreshPlayersBoard()
		currentP = self.whosturn()

		for i in range(MAX_SHIPS):
			self.drawShip(currentP.allShips[i])

		for rows in range(MAX_ROWS):
					print("")
					for cols in range(MAX_COLS):
							  print(self.board[rows][cols] , end = "")
	
	def refreshPlayersBoard(self):
		for rows in range(MAX_ROWS):
					self.board[rows] = [0] * MAX_COLS

	def initPlayers(self):
		self.player1 = Player(1)
		self.player2 = Player(2)
		print("Player 1 -- initialise your BATTLESHIPSS!!!!!")
		self.player1.initialiseShips(self)
		self.changeturn()
		print("Player 2")
		
		self.player2.initialiseShips(self)			 
		self.changeturn()

	def changeTileState(self, row, col, state):
		self.board[row][col] = state
					 
	def drawShip(self, ship):
		for i in range(ship.length):
			if not(ship.coordinates[i] == None):
					#print("drawShip ",ship.coordinates[i].row, ",", ship.coordinates[i].col)
			 		self.changeTileState(ship.coordinates[i].row ,ship.coordinates[i].col, "X")              
	

	def beginGame(self):
		while not (self.player1.hasLost() or self.player2.hasLost()):
			self.printPlayersShots()
			print("")
			self.printPlayersShips()
			print("")
			response = input("where do yo want to shoot")
			print("You sunk my battleship")
			response = input("press ENTER to end turn")
			self.changeturn()


def withinColumns(col):
		  return col >= 0 and col < MAX_COLS

def withinRows(row):
		  return row >= 0 and row < MAX_ROWS

def acceptCoordinates():
		  responseRow = int(input("please enter the row: ")) - 1
		  responseCol = int(input("please enter the column: ")) - 1
		  return [responseRow, responseCol]

def acceptDirection():
		  return int(input("which direction? 0 for horizontal, 1 for vertical")) 

def acceptShipCoordinates(nextShip):
		print(nextShip.name, " will be length: ", nextShip.length)
		responseDirection = acceptDirection() 
		nextShip.setDirection(responseDirection)
		if(nextShip.direction == DIR_HORIZONTAL):
				  print("Select cordinates for left side of the ship")
		else:
				  print("Select coordingates for top of the ship")
		getCoords = acceptCoordinates()
		if(nextShip.direction == DIR_HORIZONTAL and not withinColumns(getCoords[1] + nextShip.length)):# (getCoords[1] + nextShip.length >= MAX_COLS)):
				  print("off the horizonal")
		if(nextShip.direction == DIR_VERTICAL and not withinRows(getCoords[0] + nextShip.length)):# (getCoords[0] + nextShip.length >= MAX_ROWS)):
				  print("off the vertical")       
		nextShip.setCoords(getCoords[0], getCoords[1])

		#if responseDirection == 1:
			#validate location (make sure it's not out of the board)
			#placeVertical
		  #else:
			#placeHorizontal




def main():
	print("Welcome to Battleships")
	gameBoard = Board()
	gameBoard.initPlayers()
	gameBoard.beginGame()
	#gameBoard.printPlayersShip()
	print("Time to place the ships...")
	
		  


if __name__ == '__main__':
		  main()

