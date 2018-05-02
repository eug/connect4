import math
import operator
import sys
from copy import deepcopy
from time import time

from alphabeta import alphabeta
from connect4 import *
from constants import *
from minimax import minimax
from negamax import negamax


def get_play_options(state):
    options = []
    for j in range(0, state.width):
        for i in range(state.height - 1, -1, -1):
            if state.board[i][j] != EMPTY_SLOT: continue
            options.append((i, j))
            break
    return options

def human_vs_computer():
    current_state = State(width=7, height=6)
    current_round = 0
    current_turn = 0
    winner = 0
    
    score = score_sum_neighbors_or_win
    current_state.board[5][1] = 1
    while winner == 0:
        current_turn += 1
        current_round += 1

        # Human Turn
        sys.stdout.write('\n')
        print('-' * 20)
        print(current_state)
        options = get_play_options(current_state)
        for i in range(0, current_state.width):
            sys.stdout.write(' ' + str(i) + ' ')
        sys.stdout.write('\n-> ')

        col = int(input())
        for i, j in options:
            if col != j: continue
            current_state.board[i][j] = -1

        if done(current_state) == GAME_MIN_WINNER:
            winner = 1
            sys.stderr.write(
                str(current_round) + ',' + ',' + ',' + str(score(current_state)) + ',' + str(winner) + '\n'
            )
            sys.stdout.write('Human Win!\n')
            sys.exit(1)
        
        

        # AI Turn
        s = time()
        current_state, _score, _depth = alphabeta(current_state, 5, MAX_PLAYER, score, done, successor)
        print(time()  - s)

        max_depth = (current_state.width * current_state.height) - current_turn
        current_turn += 1

        if done(current_state) == GAME_MAX_WINNER:
            winner = 2
            print(current_state)    
            sys.stdout.write('Computer Win!\n')

        sys.stderr.write(
            str(current_round) + ',' +
            str(_depth) + ',' +
            str(max_depth + 1) + ',' +
            str(score(current_state)) + ',' +
            str(winner) + '\n'
        )



# def computer_vs_computer():
#     current_state = State(6, 7)
#     current_round = 0
#     current_turn = 0
#     winner = 0

#     score= score_sum_neighbors_or_win
#     score2 = score_max_sequence_or_win


#     while winner == 0:
#         current_turn += 1
#         current_round += 1

#         #current_state, _, nega_depth = negamax(current_state, time() + .5, MIN_PLAYER, score, done, successor)
#         current_state, _score, _depth = alphabeta(current_state, time() + .5, MIN_PLAYER, score_sum_neighbors, done, successor)
#         if done(current_state) == GAME_MIN_WINNER:
#             winner = 1
#         elif done(current_state) == GAME_DRAW:
#             print('Game Draw')
#             sys.exit(1)

#         max_depth = (current_state.width * current_state.height) - current_turn
#         print(current_round, 'Player1', _depth, max_depth, score_sum_neighbors(current_state), winner)

#         current_turn += 1
#         current_state, _score, _depth = alphabeta(current_state, time() + .5, MAX_PLAYER, score, done, successor)
        
#         if done(current_state) == GAME_MAX_WINNER:
#             winner = 2
#         elif done(current_state) == GAME_DRAW:
#             print('Game Draw')
#             sys.exit(1)
        
#         max_depth = (current_state.width * current_state.height) - current_turn
#         print(current_round, 'Player2', _depth, max_depth, score(current_state), winner)



def compare_computer_vs_computer():
    
    score1 = score_max_sequence_or_win
    score2 = score_sum_neighbors_or_win

    for j in range(0, 6):
        current_state = State(width=6, height=7)
        current_state.board[6][j] = 1
        current_round = 0
        current_turn = 0
        winner = 0
        
        print('')
        while winner == 0:
            current_round += 1

            current_turn += 1
            current_state, _score, _depth = alphabeta(current_state, 6, MIN_PLAYER, score1, done, successor)

            if done(current_state) == GAME_MIN_WINNER:
                winner = 1
            elif done(current_state) == GAME_DRAW:
                print('Game Draw')
                break

            max_depth = (current_state.width * current_state.height) - current_turn + 1
            print(current_round, 'MIN', _depth, max_depth, score1(current_state), score2(current_state), winner)
            if winner != 0:
                # print(current_state)
                break


            current_turn += 1
            current_state, _score, _depth = alphabeta(current_state, 5, MAX_PLAYER, score2, done, successor)
            
            if done(current_state) == GAME_MAX_WINNER:
                winner = 2
            elif done(current_state) == GAME_DRAW:
                print('Game Draw')
                break
            
            max_depth = (current_state.width * current_state.height) - current_turn + 1
            print(current_round, 'MAX', _depth, max_depth, score1(current_state), score2(current_state), winner)
            if winner != 0:
                # print(current_state)
                break




#computer_vs_computer()
human_vs_computer()
#compare_computer_vs_computer()

state = State(6, 7)

state.board = [
    [0,   0,  0,  0,  0,  0],
    [0,   0,  0,  0,  0,  0],
    [0,   0,  0,  0,  0,  0],
    [0,   0,  0,  0,  0,  0],
    [0,  +1, +1, -1,  0,  0],
    [+1, +1, -1, -1,  0,  0],
    [+1, +1, -1, -1, -1,  0],
]

##print(state)
#print(done(state))
#print(score_max_sequence(state))
#print(score_max_sequence_or_win(state))
#print(score_sum_neighbors(state))
#print(score_sum_neighbors_or_win(state))
#_state, _score, _depth = alphabeta(state, time() + .5, MAX_PLAYER, score, done, successor)
#print(_state)