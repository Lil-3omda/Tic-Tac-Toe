
player, opponent = 'O', 'X'
# player ->> Maximizer(Max) -----> +10
# opponent ->> Minimizer(Min) ------>-10


def isMovesLeft(board):
	for i in range(3):
		for j in range(3):
			if board[i][j] == '_':
				return True
	return False

def evaluate(b):

	for row in range(3):
		if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
			if b[row][0] == player:
				return 10
			elif b[row][0] == opponent:
				return -10

	for col in range(3):

		if b[0][col] == b[1][col] and b[1][col] == b[2][col]:

			if b[0][col] == player:
				return 10
			elif b[0][col] == opponent:
				return -10

	if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

		if b[0][0] == player:
			return 10
		elif b[0][0] == opponent:
			return -10

	if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

		if b[0][2] == player:
			return 10
		elif b[0][2] == opponent:
			return -10

	return 0


# show all the possible ways the game can go and returns the value of the board
def minimax(board, depth, isMax):
	score = evaluate(board)
	# Maximizer has won the game   "O" +10
	if score == 10:
		return score
	#  Minimizer has won the game  "X" -10
	if score == -10:
		return score
	# If there are no more moves and no winner
	if not isMovesLeft(board):
		return 0

	# maximizer's move
	if isMax:
		best = -100

		for i in range(3):
			for j in range(3):

				if board[i][j] == '_':
					board[i][j] = player
					best = max(best, minimax(board,
					                         depth + 1,
					                         not isMax))

					board[i][j] = '_'
		return best

	# minimizer's move
	else:
		best = 100

		for i in range(3):
			for j in range(3):

				if board[i][j] == '_':
					board[i][j] = opponent
					best = min(best, minimax(board, depth + 1, not isMax))

					board[i][j] = '_'
		return best


# return the best possible move for the opponent ---->  X
def findBestMove(board):
	bestVal = 100
	bestMove = (-1, -1)

	for i in range(3):
		for j in range(3):

			if board[i][j] == '_':

				board[i][j] = opponent
				moveVal = minimax(board, 0, True)
				board[i][j] = '_'

				if moveVal < bestVal:
					bestMove = (i, j)
					bestVal = moveVal
	if bestVal == -10:
		print("!*****************!********************!")
		print(" \U0001F612  \U0001F612  loser")
		print("!*****************!********************!")
	return bestMove




