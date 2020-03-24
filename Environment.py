

import numpy as np


LENGTH = 3 # Specific to Tic Tac Toe
REWARD_FOR_WINNING = 1
REWARD_FOR_LOSING_OR_DRAWING = 0


class Environment:

	def __init__(self):

		self.board = np.zeros((LENGTH , LENGTH))

		self.X = -1
		self.O =  1

		self.winner = None
		self.ended  = False

		self.number_of_states = 3**(LENGTH*LENGTH)


	def is_empty(self , i,j):
		return self.board[i,j]==0

	def reward(self , symbol):

		if not self.game_over_result():
			return 0

		if self.winner == symbol:
			return REWARD_FOR_WINNING
		else:
			return REWARD_FOR_LOSING_OR_DRAWING

	def get_state(self):

		# returns the current state as an integer based on the decimal representation of 3 states of a number
		# like binary to decimal conversion

		# from 0 to |S|-1 , where S = set of all possible values - empty , X , O
		# Some states are though not possible but they will never be reached anyway so we ignore the detail
		# Integer represented by a base-3 number

		k = 0
		h = 0

		for i in range(LENGTH):
			for j in range(LENGTH):

				if self.board[i,j]==0:
					v = 0
				elif self.board[i,j]==self.X:
					v = 1
				elif self.board[i,j]==self.O:
					v = 2

				h += (3**k)*v
				k += 1

		return h


	def game_over_result(self, force_recalculate = False):

		# Returns True if game is over and False otherwise
		# Also , gets winner instance variable if game ends and sets 'ended' instance

		if not force_recalculate and self.ended:
			return self.ended


		# ROW CEHCKS:
		for i in range(LENGTH):
			for player in (self.X , self.O):

				if self.board[i].sum() == player*LENGTH:
					self.winner = player
					self.ended = True
					return True

		# COLUMN CHECKS
		for j in range(LENGTH):
			for player in (self.X , self.O):

				if self.board[:,j].sum() == player*LENGTH:
					self.winner = player
					self.ended = True
					return True

		# DIAGONALS CHECKS
		for player in (self.X , self.O):

			# Top-left Diagonal
			if self.board.trace() == player*LENGTH:
				self.winner = player
				self.ended = True
				return True
			# Top-Right Diagonal
			if np.fliplr(self.board).trace() == player*LENGTH:
				self.winner = player
				self.ended = True
				return True


		# CHECKING DRAW
		if np.all((self.board==0) == False):
			# this checks if all places in the board are filled or not , either by 1 or -1
			# if yes , that means, game is over and since the above conditions have not been true yet ,thus DRAW

			self.winner = None
			self.ended = True
			return True


		# NO ONE WON YET , neither is the game_over with a DRAW
		self.winner = None
		return False



	def is_draw(self):

		return (self.ended and self.winner is None)


	def draw_board(self): # To display the board

		for i in range(LENGTH):
			print('--------------------')
			for j in range(LENGTH):
				print("  ",end="")
				if self.board[i,j] == self.X:
					print("X ", end = "")
				elif self.board[i,j] == self.O:
					print("O " , end = "")
				else:
					print("  ", end = "")

			print("")
		print("--------------------")
































