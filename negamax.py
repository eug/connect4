import math
from time import time

from constants import *


def negamax(state, end_time, player, score=None, done=None, successor=None, alpha=-math.inf, beta=math.inf, depth=1):
    if time() >= end_time or done(state) != GAME_NO_WINNER:
        return state, score(state), depth

    s = None
    v = -math.inf
    d = 0
    kwargs = {'score': score, 'done': done, 'successor': successor}

    for n in sorted(successor(state, player), key=score, reverse=False):
    #for n in successor(state, player):
        kwargs = {**kwargs, **{'alpha': -alpha, 'beta': -beta, 'depth': depth + 1}}
        _state, _score, _depth = negamax(n, end_time, -player, **kwargs)
        if v < -_score:
            v = -_score
            s = n
        d = max(d, _depth)
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return s, v, d
