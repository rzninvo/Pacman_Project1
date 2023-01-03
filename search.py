# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    """
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    successor_states = util.Stack()
    successor_states.push([(start_state, 'NONE', 0)])
    checked = set()
    path_found = []
    while not successor_states.isEmpty():
        search_state_list = successor_states.pop()
        cur_state = search_state_list[len(search_state_list) - 1]
        if problem.isGoalState(cur_state[0]):
            for path in search_state_list:
                if path[1] != 'NONE':
                    path_found.append(path[1])
            break
        if cur_state[0] in checked:
            continue
        checked.add(cur_state[0])
        successors_list = problem.getSuccessors(cur_state[0])
        for item in successors_list:
            copied_search_state_list = search_state_list.copy()
            copied_search_state_list.append(item)
            successor_states.push(copied_search_state_list)
    return path_found
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    successor_states = util.Queue()
    successor_states.push([(start_state, 'NONE', 0)])
    checked = set()
    path_found = []
    while not successor_states.isEmpty():
        search_state_list = successor_states.pop()
        cur_state = search_state_list[len(search_state_list) - 1]
        if problem.isGoalState(cur_state[0]):
            for path in search_state_list:
                if path[1] != 'NONE':
                    path_found.append(path[1])
            break
        if cur_state[0] in checked:
            continue
        checked.add(cur_state[0])
        successors_list = problem.getSuccessors(cur_state[0])
        for item in successors_list:
            copied_search_state_list = search_state_list.copy()
            copied_search_state_list.append(item)
            successor_states.push(copied_search_state_list)
    return path_found
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    successor_states = util.PriorityQueue()
    successor_states.push([(start_state, 'NONE', 0)], 0)
    checked = set()
    path_found = []
    while not successor_states.isEmpty():
        search_state_list = successor_states.pop()
        cur_state = search_state_list[len(search_state_list) - 1]
        if problem.isGoalState(cur_state[0]):
            for path in search_state_list:
                if path[1] != 'NONE':
                    path_found.append(path[1])
            break
        if cur_state[0] in checked:
            continue
        checked.add(cur_state[0])
        successors_list = problem.getSuccessors(cur_state[0])
        for item in successors_list:
            copied_search_state_list = search_state_list.copy()
            copied_search_state_list.append(item)
            path_cost = 0
            for cost_item in search_state_list:
                path_cost += cost_item[2]
            path_cost += item[2]
            successor_states.push(copied_search_state_list, path_cost)
    return path_found
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    successor_states = util.PriorityQueue()
    successor_states.push([(start_state, 'NONE', 0)], 0)
    checked = set()
    path_found = []
    while not successor_states.isEmpty():
        search_state_list = successor_states.pop()
        cur_state = search_state_list[len(search_state_list) - 1]
        if problem.isGoalState(cur_state[0]):
            for path in search_state_list:
                if path[1] != 'NONE':
                    path_found.append(path[1])
            break
        if cur_state[0] in checked:
            continue
        checked.add(cur_state[0])
        successors_list = problem.getSuccessors(cur_state[0])
        for item in successors_list:
            copied_search_state_list = search_state_list.copy()
            copied_search_state_list.append(item)
            path_cost = 0
            for cost_item in search_state_list:
                path_cost += cost_item[2]
            path_cost += item[2]
            h = heuristic(item[0], problem)
            successor_states.push(copied_search_state_list, path_cost + h)
    return path_found
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
