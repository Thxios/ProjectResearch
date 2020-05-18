from .heap import Heap
from .node import Node


class Exploration(Heap):
    def set_to(self, value: Node, idx):
        value.exploration_idx = idx

    @staticmethod
    def compare(v1: Node, v2: Node) -> bool:
        return v1.ucb > v2.ucb

