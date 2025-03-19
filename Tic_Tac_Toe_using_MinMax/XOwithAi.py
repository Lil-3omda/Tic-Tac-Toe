from MinMax import *
from random import randrange
import time

board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
player = "O"
def display_board(board):

	board[1][1] = "X"
	for row in range(0, 3):
		print("+-------+-------+-------+")
		print("|       " * 4)
		for col in range(0, 3):
			print("|  ", board[row][col], end="   ")
		print("|")
		print("|       " * 4)
	print("+-------+-------+-------+")


def enter_move(board):

	R, C = map(int, input("Enter your move: ").split())

	if board[R][C] != 'O' and board[R][C] != 'X':
		board[R][C] = "O"
	else:
		print("wrong move: ")
		enter_move(board)


def make_list_of_free_fields(board):

	free_board = []
	for row in range(0, 3):
		for col in range(0, 3):
			if board[row][col] != "X" and board[row][col] != "O":
				free_board.append((row, col))
	return free_board


def victory_for(board, sign):

	for row in range(3):
		if board[row][0] == sign and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
			return sign

	for column in range(3):
		if board[0][column] == sign and board[0][column] == board[1][column] and board[0][column] == board[2][column]:
			return sign

	if board[0][0] == sign and board[0][0] == board[1][1] and board[1][1] == board[2][2] or \
			board[0][2] == sign and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
		return sign

	return None


def draw_move(board):

	free_space = make_list_of_free_fields(board)

	free_space_length = len(free_space)
	if free_space_length > 0:
		bestMove = findBestMove(board)
		board[bestMove[0]][bestMove[1]] = 'X'

def start():
	status = '1'
	while status != '0':
		print("+-------+-------+-------+")
		print("Enter 1 to start the game.")
		print("Enter 0 to end the game.")
		print("+-------+-------+-------+")

		status = input('Enter your choice : ')
		if status == '0':
			break

		play(board)
		display_board(board)

		if winner != None:
			print('\n The player', winner, 'won the game ! \n')
			break
		else:
			print('Tie')

def play(board):
	free_space = len(make_list_of_free_fields(board))
	global winner
	global player

	while free_space != 0:
		display_board(board)

		if player == 'O':
			enter_move(board)
		else:
			draw_move(board)
			time.sleep(2)

		game_winner = victory_for(board, player)

		if game_winner is not None:
			winner = game_winner
			break
		else:
			if player == 'O':
				player = 'X'
			else:
				player = 'O'

		free_space = len(make_list_of_free_fields(board))


start()