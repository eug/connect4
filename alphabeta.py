import math
from time import time

from constants import *


def alphabeta(state, max_depth, player, score=None, done=None, successor=None, alpha=-math.inf, beta=math.inf, depth=1):
    if depth >= max_depth or done(state) != GAME_NO_WINNER:
        return state, score(state), depth

    s = None
    d = 0
    kwargs = {'score': score, 'done': done, 'successor': successor}

    if player == MAX_PLAYER:
        v = -math.inf
        for n in successor(state, player):

            kwargs = {**kwargs, **{'alpha': alpha, 'beta': beta, 'depth': depth + 1}}
            _state, _score, _depth = alphabeta(n, max_depth, MIN_PLAYER, **kwargs)

            if v < _score:
                v = _score
                s = n

            d = max(d, _depth)
            alpha = max(alpha, v)

            if beta <= alpha:
                break
    else:
        v = math.inf
        for n in successor(state, player):


            kwargs = {**kwargs, **{'alpha': alpha, 'beta': beta, 'depth': depth + 1}}
            _state, _score, _depth = alphabeta(n, max_depth, MAX_PLAYER, **kwargs)

            
            if v > _score:
                v = _score
                s = n

            d = max(d, _depth)
            beta = min(beta, v)

            if beta <= alpha:
                break

    return s, v, d
