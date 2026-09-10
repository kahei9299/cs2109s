"""
A Rubik's Cube like this
       0     1     2
    |-----|-----|-----|
  0 |  R  |  R  |  R  |
    |-----|-----|-----|
  1 |  G  |  G  |  G  |
    |-----|-----|-----|
  2 |  B  |  B  |  B  |
    |-----|-----|-----|
"""
import copy
import json
from ast import literal_eval
from typing import Dict, List, Optional, Tuple, Union

Action = List[Union[int, str]]

class State:
    r"""State class describes the setting of the Cube

    Args:
         layout (List[List[int]]): a 2-D list that represents the layout of the cube's faces.

    Example:
        state = State([1,2,3],[4,5,6])
        This represents the state with a layout like:
            label:    0   1   2
                0   | 1 | 2 | 3 |
                1   | 4 | 5 | 6 |

    Methods:
        left(label): move the @label row left
            returns the copy of new state (State)

        right(label): move the @label row right
            returns the copy of new state (State)

        up(label): move the @label col up
            returns the copy of new state (State)

        down(label): move the @label col down
            returns the copy of new state (State)
    """

    def __init__(self, layout: List[List[int]]):
        self.__layout = flatten(layout)
        self.__shape = []
        while isinstance(layout, list):
            self.__shape.append(len(layout))
            layout = layout[0]

    def __eq__(self, state: "State"):
        if isinstance(state, State):
            same_shape = (
                state.shape[0] == self.__shape[0] and state.shape[1] == self.__shape[1]
            )
            same_layout = all([x == y for x, y in zip(self.__layout, state.layout)])
            return same_shape and same_layout
        else:
            return False

    def __hash__(self) -> int:
        return hash(tuple(self.__layout))

    def __repr__(self) -> str:
        return str({"shape": self.__shape, "layout": self.__layout})

    def __str__(self):
        # Header
        row_str = f"{' '*5} "
        for col in range(self.shape[1]):
            row_str += f"{col:^5d} "
        cube_str = row_str + "\n"
        cube_str += f"{' '*5}+{'-----+'*self.shape[1]}\n"
        # Content
        for row in range(self.shape[0]):
            row_str = f"{row:^5d}|"
            for col in range(self.shape[1]):
                row_str += f"{str(self.layout[row*self.shape[1]+col]):^5s}|"
            cube_str += row_str + "\n"
            cube_str += f"{' '*5}+{'-----+'*self.shape[1]}\n"

        return cube_str

    @property
    def shape(self):
        return copy.deepcopy(self.__shape)

    @property
    def layout(self):
        return copy.deepcopy(self.__layout)

    def left(self, label):
        layout = self.layout
        rows, cols = self.shape
        head = layout[label * cols]
        for i in range(cols - 1):
            layout[label * cols + i] = layout[label * cols + i + 1]
        layout[(label + 1) * cols - 1] = head
        return State(unflatten_2d(layout, self.shape))

    def right(self, label):
        layout = self.layout
        rows, cols = self.shape
        tail = layout[(label + 1) * cols - 1]
        for i in range(cols - 1, 0, -1):
            layout[label * cols + i] = layout[label * cols + i - 1]
        layout[label * cols] = tail
        return State(unflatten_2d(layout, self.shape))

    def up(self, label):
        layout = self.layout
        rows, cols = self.shape
        head = layout[label]
        for i in range(rows - 1):
            layout[label + cols * i] = layout[label + cols * (i + 1)]
        layout[label + cols * (rows - 1)] = head
        return State(unflatten_2d(layout, self.shape))

    def down(self, label):
        layout = self.layout
        rows, cols = self.shape
        tail = layout[label + cols * (rows - 1)]
        for i in range(rows - 1, 0, -1):
            layout[label + cols * i] = layout[label + cols * (i - 1)]
        layout[label] = tail
        return State(unflatten_2d(layout, self.shape))


class Cube:
    r"""Cube problem class
    Args:
        initial (State): The initial state of the cube.
        goal (State): The goal state of the cube.

    Example:
        initial = State([[0, 1, 2], [3, 4, 5]])
        goal = State([[1, 0, 2], [3, 5, 4]])
        cube = Cube(initial, goal)
    """

    def __init__(self, initial: State, goal: State):
        self.__initial = initial
        self.__goal = goal
        self.__actions = self._get_actions(*self.__initial.shape)

    def __repr__(self) -> str:
        return repr({"initial": repr(self.__initial), "goal": repr(self.__goal)})

    def __str__(self) -> str:
        return f"initial:\n{str(self.__initial)}\ngoal:\n{str(self.__goal)}"

    def _get_actions(self, rows: int, cols: int):
        actions = []
        for i in range(rows):
            actions.append([i, "left"])
            actions.append([i, "right"])
        for i in range(cols):
            actions.append([i, "up"])
            actions.append([i, "down"])
        return actions

    # Observable Environment
    @property
    def initial(self):
        return copy.deepcopy(self.__initial)

    @property
    def goal(self):
        return copy.deepcopy(self.__goal)

    def actions(self, state: State):
        r"""Return the actions that can be executed in the given state.

        Args:
            state (State): the state to be checked for actions.

        Returns:
            A list of actions can be executed at the provided state.
        """
        return copy.deepcopy(self.__actions)

    # Transition Model (Deterministic)
    def result(self, source: State, action):
        r"""Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state).

        Args:
            source (State): the state to excute the action
            action: the action can be executed

        Returns:
            the state after taking action from source
        """
        assert list(action) in self.actions(
            source
        ), f"{action} is illegal action at {source}"

        label, act = action
        if act == "left":
            result = source.left(label)
        elif act == "right":
            result = source.right(label)
        elif act == "down":
            result = source.down(label)
        elif act == "up":
            result = source.up(label)
        return result

    def path_cost(self, c: float, state1: State, action, state2: State) -> float:
        r"""Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1.

        .. math::
            c + action cost

        Args:
            c (float): the cost of getting state1 from the initial state
            state1 (State): the State before executing action
            action: the action taken at state1
            state2 (State): the State after executing action

        Returns:
            the path cost of reaching state2
        """
        if self.result(state1, action) == state2:
            return c + 1

    # Goal Test
    def goal_test(self, state: State) -> bool:
        r"""Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor.

        Args:
            state (State): the state to be checked

        Return:
            True if the give state is the goal state, otherwise False
        """
        if isinstance(self.__goal, list):
            return any(state == x for x in self.__goal)
        else:
            return state == self.__goal

    # Solution Check
    def verify_solution(self, solution, _print=False):
        r"""Verify whether the given solution can reach goal state

        Args:
            solution (List): the list of actions is supposed to reach
                goal state

        Returns:
            dictionary:
                - valid (bool): whether the solution is correct (able to reach goal) or not
                - cost (number): the cost of the solution
                - error (str): error message (if any)

        Notes:
            cost == 0 means that there exists an illegal action in the solution
        """
        curr = self.__initial
        cost = 0
        for action in solution:
            if _print:
                print(curr, action)
            if list(action) not in self.actions(curr):
                return {
                    'valid': False,
                    'cost': 0,
                    'error': "Invalid moves"
                }
            next = self.result(curr, action)
            cost = self.path_cost(cost, curr, action, next)
            curr = next

        is_correct = self.goal_test(curr)

        return {
            'valid': is_correct,
            'cost': cost,
            'error': None if is_correct else "Fail to reach goal state"
        }

# Source: https://stackoverflow.com/a/47433335
def _flatten(something):
    if isinstance(something, (list, tuple, set, range)):
        for sub in something:
            yield from _flatten(sub)
    else:
        yield something


def flatten(iterable):
    return list(_flatten(iterable))


def unflatten_2d(iterable, shape):
    rows, cols = shape
    matrix = []
    for row in range(rows):
        matrix.append(iterable[row * cols : row * cols + cols])
    return matrix
