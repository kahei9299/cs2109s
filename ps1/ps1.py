### Task 1.1  - State Representation and Actions

### Task 1.2  - Initial & Goal States

### Task 1.4  - Which Search Algorithm Should We Pick?

### Task 1.5  - Completeness and Optimality

### Task 1.6  - Implement Search (No Visited Memory)

def get_initial_state(m, c):
    '''
    Create the initial state for the missionaries and cannibals problem.
    
    Parameters
    ----------    
    m: no. of missionaries
    c: no. of cannibals
    
    Returns
    ----------    
    Return the starting state derived from `m` and `c`. This could be the state representation you described in task 1.1.
    '''
    """ YOUR CODE HERE """
    return (0, 0, m, c, 0)
    """ YOUR CODE END HERE """

def get_max_steps(m, c):
    '''
    Calculate a safe upper bound on the number of moves needed to solve the problem.
    
    Parameters
    ----------    
    m: no. of missionaries
    c: no. of cannibals
    
    Returns
    ----------    
    Returns an integer representing the maximum number of steps to explore before giving up. This could be the upper bound you described in task 1.5.
    '''
    """ YOUR CODE HERE """
    return 2 * (m + 1) * (c + 1)
    """ YOUR CODE END HERE """

def is_goal(m, c, state):
    '''
    Check if the given state is a goal state.
    
    Parameters
    ----------    
    state: current state
    m: number of missionaries
    c: number of cannibals
    
    Returns
    ----------    
    Returns True if the state has reached your proposed goal state.
    '''
    """ YOUR CODE HERE """
    return state == (m, c, 0, 0, 1)
    """ YOUR CODE END HERE """

def valid_actions(state):
    '''
    Generate all valid actions from the current state.
    
    Parameters
    ----------    
    state: current state
    
    Returns
    ----------    
    Returns a set of valid actions which can be performed at the current state
    '''
    """ YOUR CODE HERE """
    m_l, c_l, m_r, c_r, boat = state
    actions = set()
    possible = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

    for m_b, c_b in possible:
        if boat == 0:
            new_m_r, new_c_r = m_r - m_b, c_r - c_b
            new_m_l, new_c_l = m_l + m_b, c_l + c_b
        else:
            new_m_l, new_c_l = m_l - m_b, c_l - c_b
            new_m_r, new_c_r = m_r + m_b, c_r + c_b

        if new_m_r < 0 or new_c_r < 0 or new_m_l < 0 or new_c_l < 0:
            continue
        if new_m_r > 0 and new_m_r < new_c_r:
            continue
        if new_m_l > 0 and new_m_l < new_c_l:
            continue
        if m_b > 0 and m_b < c_b:
            continue
        actions.add((m_b, c_b))

    return actions
    """ YOUR CODE END HERE """

def transition(state, action):
    '''
    Apply an action to the current state to get the next state.
    
    Parameters
    ----------    
    state: current state
    action: your representation from valid_actions function above for the action to take
    
    Returns
    ----------    
    Returns the state after applying the action.
    '''
    """ YOUR CODE HERE """
    m_l, c_l, m_r, c_r, boat = state
    m_b, c_b = action

    if boat == 0:
        return (m_l + m_b, c_l + c_b, m_r - m_b, c_r - c_b, 1)
    else:
        return (m_l - m_b, c_l - c_b, m_r + m_b, c_r + c_b, 0)
    """ YOUR CODE END HERE """

def mnc_search(m, c):  
    '''
    Solution should be the action taken from the root node (initial state) to 
    the leaf node (goal state) in the search tree.

    Parameters
    ----------    
    m: no. of missionaries
    c: no. of cannibals
    
    Returns
    ----------    
    Returns the solution to the problem as a tuple of steps. Each step is a tuple of two numbers x and y, indicating the number of missionaries and cannibals on the boat respectively as the boat moves from one side of the river to another. If there is no solution, return False.
    '''
    queue = []
    initial_state = get_initial_state(m, c)
    queue.append((initial_state, ()))
    max_steps = get_max_steps(m, c)

    while queue:
        state, steps = queue.pop(0)
        if is_goal(m, c, state):
            return steps
        else:
            for a in valid_actions(state):
                next_state = transition(state, a)
                if next_state is None:
                    continue
                next_steps = steps + (a,)
                if len(next_steps) <= max_steps:
                    queue.append((next_state, next_steps))
    return False

def test_task_1_6():
    # Note: These solutions are not necessarily unique! (i.e. there may be other optimal solutions.)
    assert len(valid_actions(get_initial_state(3,3))) == 3
    assert mnc_search(2,1) == ((2, 0), (1, 0), (1, 1))
    assert mnc_search(2,2) == ((1, 1), (1, 0), (2, 0), (1, 0), (1, 1))
    assert mnc_search(3,3) == ((1, 1), (1, 0), (0, 2), (0, 1), (2, 0), (1, 1), (2, 0), (0, 1), (0, 2), (1, 0), (1, 1))
    assert mnc_search(0, 0) == False

### Task 1.7 - Implement Search With Visited Memory

def mnc_search_with_visited(m,c):
    '''
    Modify your search algorithm in Task 1.6 by adding visited memory to speed it up!

    Parameters
    ----------    
    m: no. of missionaries
    c: no. of cannibals
    
    Returns
    ----------    
    Returns the solution to the problem as a tuple of steps. Each step is a tuple of two numbers x and y, indicating the number of missionaries and cannibals on the boat respectively as the boat moves from one side of the river to another. If there is no solution, return False.
    '''

    """ YOUR CODE HERE """
    queue = []
    initial_state = get_initial_state(m, c)
    queue.append((initial_state, ()))
    visited = set()
    visited.add(initial_state)

    while queue:
        state, steps = queue.pop(0)
        if is_goal(m, c, state):
            return steps
        for a in valid_actions(state):
            next_state = transition(state, a)
            if next_state is None or next_state in visited:
                continue
            visited.add(next_state)
            queue.append((next_state, steps + (a,)))
    return False
    """ YOUR CODE END HERE """

def test_task_1_7():
    # Note: These solutions are not necessarily unique! (i.e. there may be other optimal solutions.)
    assert mnc_search_with_visited(2,1) == ((1, 1), (1, 0), (2, 0))
    assert mnc_search_with_visited(2,2) == ((1, 1), (1, 0), (2, 0), (1, 0), (1, 1))
    assert mnc_search_with_visited(3,3) == ((1, 1), (1, 0), (0, 2), (0, 1), (2, 0), (1, 1), (2, 0), (0, 1), (0, 2), (1, 0), (1, 1))
    assert mnc_search_with_visited(0,0) == False

### Task 1.8 - Search With vs Without Visited Memory

import copy
import heapq
import math
import os
import random
import sys
import time

import utils
import cube

from typing import List, Tuple, Callable
from functools import partial

"""
We provide implementations for the Node and PriorityQueue classes in utils.py, but you can implement your own if you wish
"""
from utils import Node
from utils import PriorityQueue

### Task 2.1 - Design a heuristic for A* Search

def heuristic_func(problem: cube.Cube, state: cube.State) -> float:
    """
    Computes the heuristic value of a state
    
    Args:
        problem (cube.Cube): the problem to compute
        state (cube.State): the state to be evaluated
        
    Returns:
        h_n (float): the heuristic value 
    """
    h_n = 0.0
    goals = problem.goal

    """ YOUR CODE HERE """
    rows, cols = state.shape
    misplaced = sum(1 for s, g in zip(state.layout, goals.layout) if s != g)
    h_n = math.ceil(misplaced / max(rows, cols))
    """ YOUR CODE END HERE """

    return h_n

# goal state
cube_goal = {
    'initial': [['N', 'U', 'S'],
                ['N', 'U', 'S'],
                ['N', 'U', 'S']],
    'goal': [['N', 'U', 'S'],
             ['N', 'U', 'S'],
             ['N', 'U', 'S']],
    'solution': [],
}

# 3x3 cube
cube_3x3 = {
    'initial': [[1, 2, 0],
                [3, 4, 5],
                [6, 7, 8]],
    'goal': [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]],
    'solution': [[0, 'right']],
}

# one step away from goal state
cube_one_step = {
    'initial': [['S', 'N', 'U'],
                ['N', 'U', 'S'],
                ['N', 'U', 'S']],
    'goal': [['N', 'U', 'S'],
             ['N', 'U', 'S'],
             ['N', 'U', 'S']],
    'solution': [[0, 'left']],
}

# two steps away from goal state
cube_two_steps = {
    'initial': [[1, 2, 3],
                [6, 4, 5],
                [0, 7, 8]],
    'goal': [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]],
    'solution': [[0, 'right'], [0, 'down']],
}

# transposes the cube
cube_transpose = {
    'initial': [['S', 'O', 'C'],
                ['S', 'O', 'C'],
                ['S', 'O', 'C']],
    'goal': [['S', 'S', 'S'],
             ['O', 'O', 'O'],
             ['C', 'C', 'C']],
    'solution': [[2, 'right'], [1, 'left'], [1, 'down'], [2, 'up']],
}

# flips the cube
cube_flip = {
    'initial': [['N', 'U', 'S'],
                ['N', 'U', 'S'],
                ['N', 'U', 'S']],
    'goal': [['S', 'U', 'N'],
             ['N', 'S', 'U'],
             ['U', 'N', 'S']],
    'solution': [[0, 'left'], [1, 'right'], [0, 'up'], [1, 'down']],
}

# intermediate state for cube_flip
cube_flip_intermediate = {
    'initial': [['U', 'S', 'N'],
                ['N', 'U', 'S'],
                ['N', 'U', 'S']],
    'goal': [['S', 'U', 'N'],
             ['N', 'S', 'U'],
             ['U', 'N', 'S']],
    'solution': [[1, 'right'], [0, 'up'], [1, 'down']],
}


# 3x4 cube
cube_3x4 = {
    'initial': [[1, 1, 9, 0],
                [2, 2, 0, 2],
                [9, 0, 1, 9]],
    'goal': [[1, 0, 9, 2],
             [2, 1, 0, 9],
             [2, 1, 0, 9]],
    'solution': [[1, 'down'], [3, 'up'], [2, 'left']],
}

# 4x4 cube
cube_4x4 = {
    'initial': [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 0, 1, 2],
                [3, 4, 5, 6],],
    'goal': [[4, 1, 2, 3],
                [5, 6, 7, 8],
                [9, 0, 1, 2],
                [3, 4, 5, 6],],
    'solution': [[0, 'right']],
}

def test_task_2_1():
    def test_heuristic(heuristic_func, case):
        problem = cube.Cube(cube.State(case['initial']), cube.State(case['goal']))
        assert heuristic_func(problem, problem.goal) == 0, "Heuristic is not 0 at the goal state"
        assert heuristic_func(problem, problem.initial) <= len(case['solution']), "Heuristic is not admissible"
    
    test_heuristic(heuristic_func, cube_goal)
    test_heuristic(heuristic_func, cube_3x3)
    test_heuristic(heuristic_func, cube_one_step)
    test_heuristic(heuristic_func, cube_two_steps)
    test_heuristic(heuristic_func, cube_transpose)
    test_heuristic(heuristic_func, cube_flip)
    test_heuristic(heuristic_func, cube_flip_intermediate)
    test_heuristic(heuristic_func, cube_3x4)
    test_heuristic(heuristic_func, cube_4x4)

### Task 2.2 - Implement A* search 

def expand(problem, node): # Generate children nodes to be explored
    for act in problem.actions(node.state):
        state = problem.result(node.state, act)
        current_cost = problem.path_cost(node.cost, node.state, act, state)
        child = Node(parent=node, 
                    act=act, 
                    state=state, 
                    cost=current_cost)
        yield child

def astar_search(problem: cube.Cube, heuristic_func: Callable):
    r"""
    A* Search finds the solution to reach the goal from the initial.
    If no solution is found, return False.
    
    Args:
        problem (cube.Cube): Cube instance
        heuristic_func (Callable): heuristic function for the A* search

    Returns:
        solution (List[Action]): the action sequence
    """
    fail = True
    solution = []

    reached = set()
    frontier = PriorityQueue()
    initial = problem.initial
    curr = Node(parent=None, 
                act=None, 
                state=initial,
                cost=0)
    
    """ YOUR CODE HERE """
    frontier.push(heuristic_func(problem, curr.state), curr)

    while len(frontier) > 0:
        curr = frontier.pop()
        if problem.goal_test(curr.state):
            fail = False
            break
        reached.add(curr.state)
        for child in expand(problem, curr):
            if child.state not in reached:
                f = child.cost + heuristic_func(problem, child.state)
                if child not in frontier:
                    frontier.push(f, child)
                elif f < frontier[child]:
                    del frontier[child]
                    frontier.push(f, child)
    """ YOUR CODE END HERE """

    if not fail:
        while curr.parent:
            solution.append(curr.act)
            curr = curr.parent
    solution.reverse()

    if fail:
        return False
    return solution

def test_search(algorithm, case):
    problem = cube.Cube(cube.State(case['initial']), cube.State(case['goal']))
    start_time = time.perf_counter()
    solution = algorithm(problem)
    print(f"{algorithm.__name__}(goal={case['goal']}) took {time.perf_counter() - start_time:.4f} seconds")
    if solution is False:
        assert case['solution'] is False
        return
    verify_output = problem.verify_solution(solution, _print=False)
    assert verify_output['valid'], f"Fail to reach goal state with solution {solution}"
    assert verify_output['cost'] <= len(case['solution']), f"Cost is not optimal."

def test_task_2_2():
    def astar_heuristic_search(problem): 
        return astar_search(problem, heuristic_func=heuristic_func)
        
    test_search(astar_heuristic_search, cube_goal)
    test_search(astar_heuristic_search, cube_one_step)
    test_search(astar_heuristic_search, cube_transpose)
    test_search(astar_heuristic_search, cube_flip)
    test_search(astar_heuristic_search, cube_flip_intermediate)
    test_search(astar_heuristic_search, cube_3x4)

### Task 2.3 - Consistency & Admissibility

### Task 2.4 - Implement Uninformed Search

def uninformed_search(problem: cube.Cube):
    r"""
    Uninformed Search finds the solution to reach the goal from the initial.
    If no solution is found, return False.
    
    Args:
        problem (cube.Cube): Cube instance

    Returns:
        solution (List[Action]): the action sequence
    """
    """ YOUR CODE HERE """
    return astar_search(problem, lambda problem, state: 0)
    """ YOUR CODE END HERE """

def test_task_2_4():
    test_search(uninformed_search, cube_goal)
    test_search(uninformed_search, cube_one_step)
    test_search(uninformed_search, cube_transpose)
    test_search(uninformed_search, cube_flip)
    test_search(uninformed_search, cube_flip_intermediate)
    test_search(uninformed_search, cube_3x4)

### Task 2.5 - Uninformed vs Informed Search


if __name__ == '__main__':
    test_task_1_6()
    test_task_1_7()
    test_task_2_1()
    test_task_2_2()
    test_task_2_4()