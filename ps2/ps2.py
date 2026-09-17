### Task 1.1: State representation

### Task 1.2: Initial and goal states

### Task 1.3: State transitions

"""
Run this cell before you start!
"""

import random
import time

from typing import List, Tuple, Callable

def successor(route: List[int]) -> List[List[int]]:
    """
    Generates new routes to be used in the next iteration in the hill-climbing algorithm.

    Args:
        route (List[int]): The current route as a list of cities in the order of travel.

    Returns:
        new_routes (List[List[int]]): New routes to be considered.
    """
    """ YOUR CODE HERE """
    n = len(route)
    new_routes = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            new_route = route[:]
            new_route[i:j+1] = new_route[i:j+1][::-1]
            new_routes.append(new_route)
    return new_routes
    """ YOUR CODE END HERE """

def test_task_1_3():
    def test_successor(route):
        sorted_route = sorted(route)
        result = successor(route)
        assert result is not None, "Successor function returns an empty list."
        assert any(result), "Successor function returns an empty list."
        for new_route in result:
            assert len(new_route) == len(sorted_route), "New route does not have the same number of cities as the original route."
            assert sorted(new_route) == sorted_route, "New route does not contain all cities present in the original route."
    
    permutation_route = list(range(4))
    new_permutation_routes = successor(permutation_route)
    assert len(new_permutation_routes) < 24, "Your successor function may have generated too many new routes by enumerating all possible states."
    
    test_successor([1, 3, 2, 0])
    test_successor([7, 8, 6, 3, 5, 4, 9, 2, 0, 1])

### Task 1.4: Evaluation function

def evaluation_func(
    cities: int,
    distances: List[Tuple[int, int, int]],
    route: List[int]
) -> float:
    """
    Computes the evaluation score of a route

    Args:
        cities (int): The number of cities to be visited.

        distances (List[Tuple[int, int, int]]): The list of distances between every two cities. Each distance
            is represented as a tuple in the form of (c1, c2, d), where c1 and c2 are the two cities
            and d is the distance between them. The length of the list should be equal to cities *
            (cities - 1)/2.

        route (List[int]): The current route as a list of cities in the order of travel.

    Returns:
        h_n (float): the evaluation score.
    """
    """ YOUR CODE HERE """
    dist = {}
    for c1, c2, d in distances:
        dist[(c1, c2)] = d
        dist[(c2, c1)] = d
    total = 0
    for i in range(len(route)):
        total += dist[(route[i], route[(i + 1) % len(route)])]
    return -total
    """ YOUR CODE END HERE """

def test_task_1_4():
    cities = 4
    distances = [(1, 0, 10), (0, 3, 22), (2, 1, 8), (2, 3, 30), (1, 3, 25), (0, 2, 15)]
    
    
    route_1 = evaluation_func(cities, distances, [0, 1, 2, 3])
    route_2 = evaluation_func(cities, distances, [2, 1, 3, 0])
    route_3 = evaluation_func(cities, distances, [1, 3, 2, 0])
    route_4 = evaluation_func(cities, distances, [2, 3, 0, 1])
    
    assert route_1 == route_2
    assert route_1 > route_3
    assert route_1 == route_4, "Have you considered the cost to travel from the last city to the headquarter (first)?"

### Task 1.5: Explain your evaluation function

def hill_climbing(
    cities: int,
    distances: List[Tuple[int, int, int]],
    successor: Callable,
    evaluation_func: Callable
) -> List[int]:
    """
    Hill climbing finds the solution to reach the goal from the initial.

    Args:
        cities (int): The number of cities to be visited.

        distances (List[Tuple[int, int, int]]): The list of distances between every two cities. Each distance
            is represented as a tuple in the form of (c1, c2, d), where c1 and c2 are the two cities
            and d is the distance between them. The length of the list should be equal to cities *
            (cities - 1)/2.

        Successor (Callable): A function that generates new routes to be used in the next
            iteration in the hill-climbing algorithm. Will be provided on Coursemology.

        evaluation_func (Callable): A function that computes the evaluation score of a route. Will
            be provided on Coursemology.

    Returns:
        route (List[int]): The shortest route, represented by a list of cities in the order to be
            traversed.
    """
    route = random.sample(list(range(cities)), cities)
    curr_hn = evaluation_func(cities, distances, route)
    while True:
        new_routes = successor(route)
        best_new_route = max(new_routes, key=lambda x: evaluation_func(cities, distances, x))
        h_n = evaluation_func(cities, distances, best_new_route)
        if h_n <= curr_hn:
            return route

        curr_hn = h_n
        route = best_new_route


### Task 1.6: Improved hill-climbing

def hill_climbing_improved(
    cities: int,
    distances: List[Tuple[int, int, int]],
    successor: Callable,
    evaluation_func: Callable,
    hill_climbing: Callable
) -> List[int]:
    """
    Improved hill climbing that finds the solution to reach the goal from the initial.

    Args:
        cities (int): The number of cities to be visited.

        distances (List[Tuple[int, int, int]]): The list of distances between every two cities. Each distance
            is represented as a tuple in the form of (c1, c2, d), where c1 and c2 are the two cities
            and d is the distance between them. The length of the list should be equal to cities *
            (cities - 1)/2.

        successor (Callable): The successor function to be used in hill climbing. Will be
            provided on Coursemology.

        evaluation_func (Callable): The evaluation function to be used in hill climbing. Will be
            provided on Coursemology.

        hill_climbing (Callable): The hill climbing function to be used for each restart. Will be
            provided on Coursemology.

    Returns:
        route (List[int]): The shortest route, represented by a list of cities in the order to be
            traversed.
    """
    """ YOUR CODE HERE """
    best_route = None
    best_score = float('-inf')
    for _ in range(20):
        route = hill_climbing(cities, distances, successor, evaluation_func)
        score = evaluation_func(cities, distances, route)
        if score > best_score:
            best_score = score
            best_route = route
    return best_route
    """ YOUR CODE END HERE """

def test_task_1_6():
    def test_improved_hill_climbing(cities: int, distances: List[Tuple[int, int, int]], successor, evaluation_func, hill_climbing, hill_climbing_improved):
        route = hill_climbing_improved(cities, distances, successor, evaluation_func, hill_climbing)
        assert sorted(route) == list(range(cities)), "New route does not contain all cities present in the original route."
    
    cities_1 = 4
    distances_1 = [(1, 0, 10), (0, 3, 22), (2, 1, 8), (2, 3, 30), (1, 3, 25), (0, 2, 15)]
    
    test_improved_hill_climbing(cities_1, distances_1, successor, evaluation_func, hill_climbing, hill_climbing_improved)
    
    cities_2 = 10
    distances_2 = [(2, 7, 60), (1, 6, 20), (5, 4, 70), (9, 8, 90), (3, 7, 54), (2, 5, 61),
        (4, 1, 106), (0, 6, 51), (3, 1, 45), (0, 5, 86), (9, 2, 73), (8, 4, 14), (0, 1, 51),
        (9, 7, 22), (3, 2, 22), (8, 1, 120), (5, 7, 92), (5, 6, 60), (6, 2, 10), (8, 3, 78),
        (9, 6, 82), (0, 2, 41), (2, 8, 99), (7, 8, 71), (0, 9, 32), (4, 0, 73), (0, 3, 42),
        (9, 1, 80), (4, 2, 85), (5, 9, 113), (3, 6, 28), (5, 8, 81), (3, 9, 72), (9, 4, 81),
        (5, 3, 45), (7, 4, 60), (6, 8, 106), (0, 8, 85), (4, 6, 92), (7, 6, 70), (7, 0, 22),
        (7, 1, 73), (4, 3, 64), (5, 1, 80), (2, 1, 22)]
    
    test_improved_hill_climbing(cities_2, distances_2, successor, evaluation_func, hill_climbing, hill_climbing_improved)

### Task 1.7: Comparison between local search and other search algorithms

"""
Run this cell before you start!
"""

import copy
from enum import Enum
from typing import Callable, Union

class Player(Enum):
    BLACK = 'black'
    WHITE = 'white'

    # returns the opponent of the current player
    def get_opponent(self):
        if self == Player.BLACK:
            return Player.WHITE
        else:
            return Player.BLACK
        
# board row and column -> these are constant
ROW, COL = 6, 6
INF = 90129012
WIN = 21092109
MOVE_NONE = (-1, -1), (-1, -1)
TIME_LIMIT = 10

# Move / Action: ((a,b), (c,d)) means a piece moves from (a,b) to (c,d)
# State: Each state contains the board configuration and which player's turn
Score = Union[int, float]
Move = tuple[tuple[int, int], tuple[int, int]] 
Board = list[list[str]]
State = tuple[Board, Player]
Action = tuple[tuple[int, int], tuple[int, int]]


# prints out the current state of the board in a comprehensible way
def print_state(board: Board) -> None:
    horizontal_rule = "+" + ("-" * 5 + "+") * COL
    for row in board:
        print(horizontal_rule)
        print(f"|  {'  |  '.join(' ' if tile == '_' else tile for tile in row)}  |")
    print(horizontal_rule)


def heuristic(state: State) -> Score:
    """
    Returns the score of the current position from black's perspective.

    Parameters
    ----------
    state: A tuple containing board and current_player information. Board is a 2D list of lists. Contains characters "B", "W", and "_",
            representing black pawn, white pawn, and empty cell, respectively. current_player is the colour of the current player to move.

    Returns
    -------
    An evaluation (as a Score).
    """
    bcount = 0
    wcount = 0
    board = state[0]
    for r, row in enumerate(board):
        for tile in row:
            if tile == "B":
                if r == 5:
                    return WIN
                bcount += 1
            elif tile == "W":
                if r == 0:
                    return -WIN
                wcount += 1
    if wcount == 0:
        return WIN
    if bcount == 0:
        return -WIN
    return bcount - wcount

### Task 2.1: Generate Valid Actions

def valid_actions(
    state: State
) -> set[Action]:
    """
    Generates a list containing all possible actions in a particular position for the current player
    to move. Return an empty set if there are no possible actions.

    Parameters
    ----------
    state: A tuple containing board and current_player information. Board is a 2D list of lists. Contains characters "B", "W", and "_",
        representing black pawn, white pawn, and empty cell, respectively. current_player is the colour of the current player to move.

    Returns
    -------
    A set of Actions.
    """
    """ YOUR CODE HERE """
    board, player = state
    actions = set()
    piece = 'B' if player == Player.BLACK else 'W'
    dr = 1 if player == Player.BLACK else -1

    for r in range(ROW):
        for c in range(COL):
            if board[r][c] != piece:
                continue
            nr = r + dr
            if nr < 0 or nr >= ROW:
                continue
            if board[nr][c] == '_':
                actions.add(((r, c), (nr, c)))
            for nc in (c - 1, c + 1):
                if 0 <= nc < COL and board[nr][nc] != piece:
                    actions.add(((r, c), (nr, nc)))
    return actions
    """ YOUR CODE END HERE """

def test_task_2_1():
    def test_valid_actions():
        # Test case 1: A single black pawn in the middle with all three forward moves possible
        board_1 = [
            list("______"),
            list("__B___"),
            list("______"),
            list("______"),
            list("______"),
            list("______"),
        ]
        state_1 = (board_1, Player.BLACK)
        actions_1 = valid_actions(state_1)
        expected_actions_1 = {
            ((1, 2), (2, 1)), 
            ((1, 2), (2, 2)), 
            ((1, 2), (2, 3))
        }
        assert actions_1 == expected_actions_1, "valid_actions failed for a single black pawn with 3 empty forward squares."
    
        # Test case 2: A single white pawn at the edge with two forward moves possible
        board_2 = [
            list("______"),
            list("______"),
            list("______"),
            list("______"),
            list("W_____"),
            list("______"),
        ]
        state_2 = (board_2, Player.WHITE)
        actions_2 = valid_actions(state_2)
        expected_actions_2 = {
            ((4, 0), (3, 0)), 
            ((4, 0), (3, 1))
        }
        assert actions_2 == expected_actions_2, "valid_actions failed for a single white pawn at the edge."
    
        # Test case 3: Mixed moves for a black pawn
        board_3 = [
            list("______"),
            list("___B__"),
            list("__W_W_"),
            list("______"),
            list("______"),
            list("______"),
        ]
        state_3 = (board_3, Player.BLACK)
        actions_3 = valid_actions(state_3)
        expected_actions_3 = {
            ((1, 3), (2, 2)),
            ((1, 3), (2, 3)),
            ((1, 3), (2, 4))
        }
        assert actions_3 == expected_actions_3, "valid_actions failed for Black's mixed moves (move and capture)."
    
        # Test case 4: A fully blocked black pawn has no moves.
        board_4 = [
            list("______"),
            list("__B___"),
            list("_BWB__"),
            list("______"),
            list("______"),
            list("______"),
        ]
        state_4 = (board_4, Player.BLACK)
        actions_4 = valid_actions(state_4)
        pawn_at_1_2_moves = {action for action in actions_4 if action[0] == (1, 2)}
        assert len(pawn_at_1_2_moves) == 0, "valid_actions failed for a fully blocked pawn; it should have no moves."
    
    
    test_valid_actions()
    print("All valid_actions tests passed!")

### Task 2.2: Transition function

def transition(
        state: State,
        action: Action,
    ) -> State:
    """
    Updates the board configuration by creating a new board with updated values

    Parameters
    ----------
    state: A tuple containing board and current_player information. Board is a 2D list of lists. Contains characters "B", "W", and "_",
        representing black pawn, white pawn, and empty cell, respectively. current_player is the colour of the current player to move.
    action: A tuple containing source and destination position of the pawn.

    Returns
    -------
    The new State.
    """
    """ YOUR CODE HERE """
    board, player = state
    new_board = [row[:] for row in board]
    (sr, sc), (dr, dc) = action
    new_board[dr][dc] = new_board[sr][sc]
    new_board[sr][sc] = '_'
    return (new_board, player.get_opponent())
    """ YOUR CODE END HERE """

def test_task_2_2():
    def test_transition():
        # Test case 1: Black pawn moves forward
        board_1 = [
            list("______"),
            list("__B___"),
            list("______"),
            list("______"),
            list("______"),
            list("______"),
        ]
        state_1 = (board_1, Player.BLACK)
        action_1 = ((1, 2), (2, 2))
        new_state_1 = transition(state_1, action_1)
        expected_board_1 = [
            list("______"),
            list("______"),
            list("__B___"),
            list("______"),
            list("______"),
            list("______"),
        ]
        assert new_state_1[0] == expected_board_1, "transition failed for Black's forward move."
        assert new_state_1[1] == Player.WHITE, "transition failed to switch player"
    
        # Test case 2: White pawn captures a black pawn
        board_2 = [
            list("______"),
            list("__B___"),
            list("_W____"),
            list("______"),
            list("______"),
            list("______"),
        ]
        state_2 = (board_2, Player.WHITE)
        action_2 = ((2, 1), (1, 2))
        new_state_2 = transition(state_2, action_2)
        expected_board_2 = [
            list("______"),
            list("__W___"),
            list("______"),
            list("______"),
            list("______"),
            list("______"),
        ]
        assert new_state_2[0] == expected_board_2, "transition failed for White's capture move."
        assert new_state_2[1] == Player.BLACK, "transition failed to switch player"
        
        # Test case 3: Original board is not modified
        original_board = [
            list("______"),
            list("__B___"),
            list("______"),
            list("______"),
            list("______"),
            list("______"),
        ]
        original_board_copy = copy.deepcopy(original_board)
        state_3 = (original_board, Player.BLACK)
        action_3 = ((1, 2), (2, 2))
        transition(state_3, action_3)
        assert original_board == original_board_copy, "transition function should not modify the original board."
    
    test_transition()
    print("All transition tests passed!")

### Task 2.3: Detect Terminal States

def is_terminal(state: State) -> bool:
    """
    Returns True if game is over.

    Parameters
    ----------
    state: A tuple containing board and current_player information. Board is a 2D list of lists. Contains characters "B", "W", and "_",
        representing black pawn, white pawn, and empty cell, respectively. current_player is the colour of the current player to move.

    Returns
    -------
    A bool representing whether the game is over.
    """
    """ YOUR CODE HERE """
    board, player = state
    has_black = False
    has_white = False
    for r in range(ROW):
        for c in range(COL):
            if board[r][c] == 'B':
                if r == 5:
                    return True
                has_black = True
            elif board[r][c] == 'W':
                if r == 0:
                    return True
                has_white = True
    return not has_black or not has_white
    """ YOUR CODE END HERE """

def test_task_2_3():
    def test_is_terminal():
        # Test case 1: Black wins by reaching the end
        board_1 = [
            list("______"), list("______"), list("______"),
            list("______"), list("______"), list("___B__"),
        ]
        assert is_terminal((board_1, Player.BLACK)) is True, "is_terminal failed for Black's win condition."
    
        # Test case 2: White wins by reaching the end
        board_2 = [
            list("__W___"), list("______"), list("______"),
            list("______"), list("______"), list("______"),
        ]
        assert is_terminal((board_2, Player.WHITE)) is True, "is_terminal failed for White's win condition."
    
        # Test case 3: White wins by eliminating all black pieces
        board_3 = [
            list("______"), list("__W___"), list("______"),
            list("______"), list("______"), list("___W__"),
        ]
        assert is_terminal((board_3, Player.WHITE)) is True, "is_terminal failed when Black has no pieces."
    
        # Test case 4: Non-terminal state
        board_4 = [
            list("______"), 
            list("__B___"), 
            list("______"),
            list("_W____"), 
            list("______"), 
            list("______"),
        ]
        assert is_terminal((board_4, Player.BLACK)) is False, "is_terminal failed for a non-terminal state."
    
    
    
    test_is_terminal()
    print("All is_terminal tests passed!")

### Task 2.4: Utility of terminal states

def utility(state: State) -> int:
    """
    Returns score of the terminal state from the point of view of black.

    Parameters
    ----------
    state: A tuple containing board and current_player information. Board is a 2D list of lists. Contains characters "B", "W", and "_",
        representing black pawn, white pawn, and empty cell, respectively. current_player is the colour of the current player to move.

    Returns
    -------
    int representing the score.
    """
    """ YOUR CODE HERE """
    board, player = state
    has_black = False
    has_white = False
    for r in range(ROW):
        for c in range(COL):
            if board[r][c] == 'B':
                if r == 5:
                    return WIN
                has_black = True
            elif board[r][c] == 'W':
                if r == 0:
                    return -WIN
                has_white = True
    if not has_white:
        return WIN
    if not has_black:
        return -WIN
    return 0
    """ YOUR CODE END HERE """

def test_task_2_4():
    def test_utility():
        # Test case 1: Black wins
        board_1 = [
            list("______"), list("______"), list("______"),
            list("______"), list("______"), list("B_____"),
        ]
        assert utility((board_1, Player.BLACK)) == WIN, "utility failed for Black's win."
    
        # Test case 2: White wins
        board_2 = [
            list("W_____"), list("______"), list("______"),
            list("______"), list("______"), list("______"),
        ]
        assert utility((board_2, Player.WHITE)) == -WIN, "utility failed for White's win."
    
        # Test case 3: Black wins (no white pieces)
        board_3 = [
            list("______"), list("B_____"), list("______"),
            list("______"), list("______"), list("______"),
        ]
        assert utility((board_3, Player.BLACK)) == WIN, "utility failed for Black's win by eliminating opponent."
    
    
    test_utility()
    print("All utility tests passed!")

def evaluate(state: State) -> int:
    """
    Returns the value of heuristic(state) if it has hit max_depth, otherwise calls utility(state) if it is a terminal state

    Parameters
    ----------
    state: A tuple containing board and current_player information. Board is a 2D list of lists. Contains characters "B", "W", and "_",
        representing black pawn, white pawn, and empty cell, respectively. current_player is the colour of the current player to move.

    Returns
    -------
    int representing the score.
    """
    #It has hit max_depth
    if not is_terminal(state):
        return heuristic(state)
    
    return utility(state)

def minimax(
    board: Board,
    depth: int,
    max_depth: int,
    current_player: Player,
) -> tuple[Score, Action]:
    """
    Finds the best move for the current player and corresponding evaluation from black's
    perspective for the input board state. Return MOVE_NONE if no move is possible
    (e.g. when the game is over).

    Parameters
    ----------
    board: 2D list of lists. Contains characters "B", "W", and "_",
        representing black pawn, white pawn, and empty cell, respectively. Your function may modify
        the board internally, but the original board passed as an argument must remain unchanged.

    depth: int, the depth to search for the best move. When this is equal to `max_depth`, you
        should get the evaluation of the position using the provided heuristic function.

    max_depth: int, the maximum depth for cutoff.

    current_player: Player, the colour of the current player to move.

    Returns
    -------
    A tuple (evaluation, ((src_row, src_col), (dst_row, dst_col))):
    evaluation: the best score that the current player to move can achieve.
    src_row, src_col: position of the pawn to move.
    dst_row, dst_col: position to move the pawn to.
    """

    state = (board,current_player)
    
    if depth == max_depth or is_terminal(state):
        return evaluate(state), MOVE_NONE

    if current_player == Player.BLACK:
        best_score = -INF
    else:
        best_score = INF

    best_move = MOVE_NONE
    next_player = current_player.get_opponent()

    for action in valid_actions(state):
        child = transition(state, action)
        new_board = child[0]
        score = minimax(new_board, depth + 1, max_depth, next_player)[0]

        if current_player == Player.BLACK:
            if score > best_score:
                best_score = score
                best_move = action
        else:
            if score < best_score:
                best_score = score
                best_move = action

    return best_score, best_move

board_31 = [
    list("______"),
    list("__BB__"),
    list("____BB"),
    list("WBW_B_"),
    list("____WW"),
    list("_WW___"),
]

board_32 = [
    list("______"),
    list("__B___"),
    list("W_____"),
    list("___B_B"),
    list("__W___"),
    list("______"),
]


def invoke_search_fn(search_fn, board, max_depth,current_player):
    return search_fn(board, 0, max_depth,current_player)

def test_search(search_fn, board, max_depth, current_player, expected_score, expected_moves):
    score, move = invoke_search_fn(
        search_fn,
        board,
        max_depth,
        current_player,
    )

    assert score == expected_score, (
        f"Final evaluation score should be {expected_score} "
        f"instead of {score}."
    )

    assert move in expected_moves, (
        f"Your function does not correctly move "
        f"{current_player.value}'s pieces despite having "
        f"the correct evaluation."
    )


test_search(minimax, board_31, 3, Player.BLACK, WIN, [ ((3, 4), (4, 5)), ])

test_search(minimax, board_32, 3, Player.WHITE, -WIN, [((2, 0), (1, 0)),((2, 0), (1, 1))])

print("All minimax search tests passed!")

### Task 2.5: Integrate alpha-beta pruning into minimax

def minimax_alpha_beta(
    board: Board,
    depth: int,
    max_depth: int,
    alpha: Score,
    beta: Score,
    current_player: Player
) -> tuple[Score, Move]:
    """
    Finds the best move for the current player and corresponding evaluation from black's
    perspective for the input board state. Return MOVE_NONE if no move is possible
    (e.g. when the game is over).

    Parameters
    ----------
    board: 2D list of lists. Contains characters "B", "W", and "_",
        representing black pawn, white pawn, and empty cell, respectively. Your function may modify
        the board internally, but the original board passed as an argument must remain unchanged.

    depth: int, the depth to search for the best move. When this is equal to `max_depth`, you
        should get the evaluation of the position using the provided heuristic function.

    max_depth: int, the maximum depth for cutoff.

    alpha: Score. The alpha value in a given state.

    beta: Score. The beta value in a given state.

    current_player: Player, the colour of the current player
        to move.

    Returns
    -------
    A tuple (evaluation, ((src_row, src_col), (dst_row, dst_col))):
    evaluation: the best score that the current player to move can achieve.
    src_row, src_col: position of the pawn to move.
    dst_row, dst_col: position to move the pawn to.
    """
    """ YOUR CODE HERE """
    state = (board, current_player)

    if depth == max_depth or is_terminal(state):
        score = utility(state) if is_terminal(state) else heuristic(state)
        return score, MOVE_NONE

    best_move = MOVE_NONE
    next_player = current_player.get_opponent()

    if current_player == Player.BLACK:
        best_score = -INF
        for action in valid_actions(state):
            child = transition(state, action)
            score = minimax_alpha_beta(child[0], depth + 1, max_depth, alpha, beta, next_player)[0]
            if score > best_score:
                best_score = score
                best_move = action
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
    else:
        best_score = INF
        for action in valid_actions(state):
            child = transition(state, action)
            score = minimax_alpha_beta(child[0], depth + 1, max_depth, alpha, beta, next_player)[0]
            if score < best_score:
                best_score = score
                best_move = action
            beta = min(beta, best_score)
            if beta <= alpha:
                break

    return best_score, best_move
    """ YOUR CODE END HERE """

board_41 = [
    list("______"),
    list("__BB__"),
    list("____BB"),
    list("WBW_B_"),
    list("____WW"),
    list("_WW___"),
]

board_33 = [
    list("______"),
    list("__B___"),
    list("W_____"),
    list("___B_B"),
    list("__W___"),
    list("______"),
]

preservation_board = [
    list("___B__"),
    list("______"),
    list("_B__B_"),
    list("W____W"),
    list("___W__"),
    list("_W____"),
]

def invoke_search_fn(search_fn, board, max_depth, current_player):
    if "alpha_beta" in search_fn.__name__:
        return search_fn(board, 0, max_depth, -INF, INF, current_player)
    else:
        return search_fn(board, 0, max_depth, current_player)

def test_board_preservation(search_fn):
    control_board = copy.deepcopy(preservation_board)
    input_board = copy.deepcopy(preservation_board)
    invoke_search_fn(search_fn, input_board, 2, Player.BLACK)
    assert control_board == input_board, "One or more of your functions may be modifying the original board."

def test_search(search_fn, board, max_depth, current_player, expected_score, expected_moves):
    score, move = invoke_search_fn(search_fn, board, max_depth, current_player)
    assert score == expected_score, f"Final evaluation score should be {expected_score} instead of {score}."
    assert move in expected_moves, f"Your function does not correctly move {current_player.value}'s pieces despite having the correct evaluation."

def test_task_2_5():
    test_board_preservation(minimax_alpha_beta)
    test_search(minimax_alpha_beta, board_41, 3, Player.BLACK, WIN, [((3, 4), (4, 5))])
    test_search(minimax_alpha_beta, board_33, 3, Player.WHITE, -WIN, [((2, 0), (1, 0)), ((2, 0), (1, 1))])

### Task 2.6: Implement an improved heuristic function

def improved_evaluate(state: State) -> Score:
    """
    Returns the score of the current position with an improved heuristic.

    Parameters
    ----------
    state: A tuple containing the board and current player.

    Returns
    -------
    An improved evaluation (as a Score).
    """
    """ YOUR CODE HERE """
    board, player = state
    black_score = 0
    white_score = 0
    bcount = 0
    wcount = 0
    for r in range(ROW):
        for c in range(COL):
            if board[r][c] == 'B':
                if r == 5:
                    return WIN
                black_score += r * r
                bcount += 1
            elif board[r][c] == 'W':
                if r == 0:
                    return -WIN
                white_score += (5 - r) * (5 - r)
                wcount += 1
    if wcount == 0:
        return WIN
    if bcount == 0:
        return -WIN
    return black_score - white_score
    """ YOUR CODE END HERE """

def test_task_2_6():
    board_51 = [
        list("___B__"),
        list("______"),
        list("______"),
        list("__B___"),
        list("_WWW__"),
        list("______"),
    ]
    
    board_52 = [
        list("___BW_"),
        list("___W__"),
        list("______"),
        list("______"),
        list("______"),
        list("______"),
    ]
    
    board_53 = [
        list("______"),
        list("______"),
        list("______"),
        list("__B___"),
        list("______"),
        list("______"),
    ]
    
    board_54 = [
        list("__B___"),
        list("__WB__"),
        list("______"),
        list("______"),
        list("______"),
        list("______"),
    ]
    
    assert improved_evaluate((board_51, Player.BLACK)) > heuristic((board_51, Player.BLACK)), "Your improved evaluation function should return higher than the original heuristic, as black is winning."
    assert improved_evaluate((board_52, Player.BLACK)) == -WIN, "Your improved evaluation function does not correctly evaluate won positions."
    assert improved_evaluate((board_53, Player.BLACK)) == WIN, "Your improved evaluation function does not correctly evaluate won positions."
    assert improved_evaluate((board_54, Player.BLACK)) < heuristic((board_54, Player.BLACK)), "Your improved evaluation function should return smaller than the original heuristic, as white is winning."


if __name__ == '__main__':
    test_task_1_3()
    test_task_1_4()
    test_task_1_6()
    test_task_2_1()
    test_task_2_2()
    test_task_2_3()
    test_task_2_4()
    test_task_2_5()
    test_task_2_6()