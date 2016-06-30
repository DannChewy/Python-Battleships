MAX_COLS = 10
MAX_ROWS = 10
MAX_SHIPS = 2
DIR_HORIZONTAL = 0
DIR_VERTICAL = 1
TILE_STATUS_SHIP_ALIVE = 0
DEFAULT_BOARD_TILE = 0

import os

def clear():
	print("\n" * 10)
	if os.name == 'posix':
		os.system('clear')

	elif os.name in ('ce', 'nt', 'dos'):
		os.system('cls')

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
		if(nextShip.direction == DIR_HORIZONTAL and not withinColumns(getCoords[1] + nextShip.length)):
				  print("off the horizonal")
		if(nextShip.direction == DIR_VERTICAL and not withinRows(getCoords[0] + nextShip.length)):
				  print("off the vertical")       
		nextShip.setCoords(getCoords[0], getCoords[1])