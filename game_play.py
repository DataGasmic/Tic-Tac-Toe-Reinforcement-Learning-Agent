# TIC - TAC - TOE 


import numpy as np  
from Agent import Agent
from Human import Human
from Environment import Environment


LENGTH = 3
EPISODES = 10_000


def get_state_hash_and_winner(env , i=0 , j=0):

	''' This function returns a state, winner, ended triple to the functions'''

	results = []

	for v in (0,env.X , env.O):

		env.board[i,j] = v

		if j==2:

			if i==2:

				# Board is full collect the result
				state = env.get_state()
				ended = env.game_over_result(force_recalculate = True)
				winner = env.winner

				results.append((state, winner, ended))

			else :

				results += get_state_hash_and_winner( env , i+1 , j)

		else:

			results += get_state_hash_and_winner(env , i , j+1)

	return results 


def initialise_X(env , state_winner_ended_triple):

	V = np.zeros(env.number_of_states)

	for state , winner , ended in state_winner_ended_triple:

		if ended:
			if winner == env.X:
				v=1
			else:
				v=0

		else:
			v=0.5

		V[state] = v

	return V


def initialise_O(env , state_winner_ended_triple):

	V = np.zeros(env.number_of_states)

	for state , winner , ended in state_winner_ended_triple:

		if ended:
			if winner == env.O:
				v=1
			else:
				v=0

		else:
			v=0.5

		V[state] = v

	return V



def game_play(p1 , p2 , env , draw = False):

	current_player = None

	while not env.game_over_result():

		if current_player == p1:
			current_player = p2
		else:
			current_player = p1

		if draw:

			if draw == 1 and current_player == p1:
				env.draw_board()

			if draw == 2 and current_player == p2:
				env.draw_board()


		current_player.action(env)

		# Update State Histories

		state = env.get_state()
		p1.update_state_history(state)
		p2.update_state_history(state)


	if draw:
		env.draw_board()

	# Do the Value function update after the episode
	p1.update(env)
	p2.update(env)



# MAIN SECTION


p1 = Agent()
p2 = Agent()

env = Environment()
state_winner_ended_triple = get_state_hash_and_winner(env)


V_x = initialise_X(env , state_winner_ended_triple)
p1.set_value_func(V_x)

V_o = initialise_O(env , state_winner_ended_triple)
p2.set_value_func(V_o)

p1.set_symbol(env.X)
p2.set_symbol(env.O)

for t in range(EPISODES):

	if t % 200 == 0:
		print(t)

	game_play(p1 , p2 , Environment())



# Play Human vs Agent

human = Human()
human.set_symbol(env.O)

while True:

	p1.set_verbose(True)
	game_play(p1 , human , Environment() , draw = 2)

	answer = input("Play Again ? [ Y/n ] :: ")

	if answer and answer.lower()[0] == 'n':
		break












































