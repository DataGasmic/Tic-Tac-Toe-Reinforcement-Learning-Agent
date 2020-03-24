class Human:

	def __init__(self):

		pass

	def set_symbol(self , symbol):
		self.symbol = symbol

	def action(self , env):

		while True:

			# Break as soon as we make a legal move
			move = input(" Enter the coordinates i,j for your next move ( i,j = 0/1/2 ) :: ")
			i,j = move.split(',')
			i , j = int(i) , int(j)

			if env.is_empty(i,j):
				env.board[i,j] = self.symbol
				break 



	def update(self,env):
		pass

	def update_state_history(self , s):
		pass


