from lib import *

from .navigator import Exploration
from .policy import PolicyFinder
from .value import ValueFinder

from Gomoku.board import Board


class Node:
    ucb_weight = np.sqrt(2)

    def __init__(
            self,
            state: Board,           # current state of board
            action: np.ndarray,     # next action
            turn: int,              # turn of action
            depth: int,             #
            parent=None
    ):
        self.state = state
        self.action = action
        self.turn = turn
        self.depth = depth

        self.visit = 1
        self.win = 0
        self.parent = parent
        if self.parent is None:
            self.root = False
            self.total_visit = 1
        else:
            self.root = True
            self.total_visit = self.parent.total_visit + self.parent.visit

        self.next_state = copy.deepcopy(state)
        self.next_state.put(action[0], action[1], self.turn)

        self.ucb = 0.
        self.value = 0.
        self.exploration_idx = -1

        self.calculate_ucb()

        self.evaluated = False
        self.children = Exploration()
        # self.children = []
        self.policy_finder = PolicyFinder(self.state, self.turn)

        # if not self.root:
        #     self.backpropagate()

    def explore(self):
        if not self.evaluated:
            self.evaluate()
            self.backpropagate()
            self.evaluated = True
            return

        self.expand()
        self.children.top().explore()

    def select(self):
        self.parent = None
        self.root = True

    def expand(self):
        next_action = self.policy_finder.get_next_action()
        if next_action is None:
            return
        next_turn = WHITE if self.turn == BLACK else BLACK
        child = Node(self.next_state, next_action, next_turn, self.depth + 1, self.total_visit + self.visit)
        self.children.push(child)

    def backpropagate(self):
        pass

    def evaluate(self):
        self.value = ValueFinder.network(self.state, self.turn)

    def calculate_ucb(self):
        self.ucb = self.value + Node.ucb_weight * np.sqrt(np.log(self.total_visit, self.visit))

