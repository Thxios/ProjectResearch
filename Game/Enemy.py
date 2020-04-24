from .imports import *
from .Object import Object


class Enemy(Object):
    symbol = vector(1, 0, 0)


class Obstacle(Object):
    symbol = vector(1, 0, 1)

