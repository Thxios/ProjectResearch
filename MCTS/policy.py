from lib import *

from Gomoku.board import Board


class PolicyFinder:
    def __init__(self, state: Board, turn):
        self.state = state
        self.turn = turn

        self.policy_board = None
        self.policy = None
        self.network()

    def network(self):
        # for test
        self.policy_board = np.zeros((15, 15), dtype=np.float)

        self.policy = [*np.argwhere(self.policy_board)]
        self.policy.sort(key=lambda action: self.policy_board[action[0], action[1]])

    def get_next_action(self):
        action = self.policy.pop()
        while not self.state.valid(action[0], action[1], self.turn):
            if len(self.policy) == 0:
                return None
            action = self.policy.pop()
        return action

