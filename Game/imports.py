
import numpy as np
from typing import *

from .config import *


def vector(*args, dtype=None):
    if dtype is None:
        return np.array(args)
    return np.array(args, dtype=dtype)
