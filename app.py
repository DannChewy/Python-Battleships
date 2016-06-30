import game
from game import Game

def main():
	print("Welcome to Battleships")
	gameBoard = Game()
	gameBoard.initPlayers()
	gameBoard.beginGame()

if __name__ == '__main__':
	main()
