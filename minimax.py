import math
from time import time

from constants import *


def minimax(state, end_time, player, score=None, done=None, successor=None, depth=1):
    if time() >= end_time or done(state) != GAME_NO_WINNER:
        return state, score(state), depth

    s = None
    v = None
    d = 0
    kwargs = {'score': score, 'done': done, 'successor': successor, 'depth': depth + 1}

    if player == MAX_PLAYER:
        v = -math.inf
        for n in successor(state, player):
            _state, _score, _depth = minimax(n, end_time, MIN_PLAYER, **kwargs)
            if v < _score:
                v = _score
                s = n
            d = max(d, _depth)
    else:
        v = math.inf
        for n in successor(state, player):
            _state, _score, _depth = minimax(n, end_time, MAX_PLAYER, **kwargs)
            if v > _score:
                v = _score
                s = n
            d = max(d, _depth)
    return s, v, d
