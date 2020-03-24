

# Importing necessary libraries

import numpy as np


# Setting Board Constants

LENGTH = 3    # For Tic-Tac-Toe

class Agent:
	'''The Agent class handles the functionalities oif the agent'''

	def __init__( self , epsilon = 0.1 , learning_rate = 0.5 ):
		self.epsilon = epsilon
		self.learning_rate = learning_rate
		self.verbose = False
		self.state_history = []

	def set_symbol( self , symbol ):
		self.symbol = symbol
		
	def set_value_func(self , value_func ):
		self.value_func = value_func

	def set_verbose(self , v):
		self.verbose = v

	def reset_history(self ):
		self.state_history = []


	def action(self, env):

		best_state = None

		# Choosing an action , random or reward based - Epsilon Greedy strategy

		if np.random.rand() < self.epsilon:

			if self.verbose :

				print("Taking a Random action from possible set of actions ")


			# Finding the potential action states
			possible_moves = []

			for i in range(LENGTH):
				for j in range(LENGTH):
					if env.is_empty(i,j):
						possible_moves.append((i,j))

			# Selecting randomly a choice between possilbe states

			choice = np.random.choice(len(possible_moves))
			move = possible_moves[choice]


		else:

			# Choosing the best action based on current values of the states
			# Loop through all the possible moves and track the best value and make a mve
			pos2value = {}

			move = None
			best_value = -1

			for i in range(LENGTH):
				for j in range(LENGTH):

					if env.is_empty(i,j):
						# What if we made this move and land in this state

						env.board[i,j] = self.symbol
						state = env.get_state()
						pos2value[(i,j)] = self.value_func[state]
						env.board[i,j] = 0

						if self.value_func[state]>best_value:
							best_value = self.value_func[state]
							best_state = state
							move = (i,j)

		# Handling the Verbose , if True , draw the board
			if self.verbose:

				print("Taking a Greedy Action based on the Value Function")

				for i in range(LENGTH):
					print('--------------------')

					for j in range(LENGTH):

						if env.is_empty(i,j):
							# Print the value based on the value function values found above
							print("{:.2f}|".format(pos2value[(i,j)]), end = "")

						else:

							print("  " ,end="")
							if env.board[i,j] == env.X:
								print("X |" , end = "")
							elif env.board[i,j] == env.O:
								print("O |" , end = "")
							else:
								#print("WHY HERE  - Corner Case")
								print("  |" , end = "")

					print("")
				print("--------------------")

		env.board[ move[0] , move[1] ] = self.symbol


	def update_state_history(self , s):

		self.state_history.append(s)



	def update(self , env):

		# The Real Reinforcement Learning Part - where we are backtracking
		# FORMULA
		# value_func(prev_state) = value_func(prev_state) + learning_rate(value_func(next_state) - value_func(prev_state))

		# where , value_func(next_state) = REWARD if it's the most current ( last state )
		# ONLY DONE AT THE END OF THE EPISODE

		reward = env.reward(self.symbol)
		target = reward # From the last , after the episode ends

		for prev in reversed(self.state_history):

			value = self.value_func[prev] + self.learning_rate*(target - self.value_func[prev])
			self.value_func[prev] = value
			target = value

		self.reset_history()
























































