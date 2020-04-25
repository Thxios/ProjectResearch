
import numpy as np
from typing import *
from random import randint

from .config import *


def vector(*args, dtype=None):
    if dtype is None:
        return np.array(args)
    return np.array(args, dtype=dtype)

def clamp(value, minimum, maximum):
    return max(min(value, maximum), minimum)
