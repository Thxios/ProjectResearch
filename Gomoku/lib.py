import numpy as np
from typing import *


def vector(*args, dtype=None):
    if dtype is None:
        return np.array(args)
    return np.array(args, dtype=dtype)


EMPTY = 0
BLACK = 1
WHITE = 2

directions = vector(
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
)

