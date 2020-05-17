import numpy as np


class Node:
    ucb_weight = 1.

    def __init__(
            self,
            state: np.ndarray,
            action: np.ndarray,
            turn: int,
            depth: int,
            total_visit: int
    ):
        self.state = state
        self.action = action
        self.turn = turn
        self.depth = depth

        self.next_state = state.copy()
        self.next_state[self.action[0], self.action[1]] = self.turn

        self.total_visit = total_visit
        self.visit = 1
        self.win = 0

        self.ucb = 0.
        self.exploration_idx = -1

        self.value = 0.
        self.exploitation_idx = -1

        self.calculate_ucb()

    def calculate_ucb(self):
        self.ucb = self.value + Node.ucb_weight * np.sqrt(np.log(self.total_visit, self.visit))

    def calculate_value(self):
        self.value = self.win / self.visit

