from itertools import count
import heapq
counter = count()

class Node:
    #Create a node to actually represent states and be able to find parent nodes, and costs
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h
        self.id = next(counter)

    def __lt__(self, other):
        return (self.f, self.id) < (other.f, other.id)
    
    def path(self):
        cur = self
        result = []
        while cur:
            result.append(cur.state)
            cur = cur.parent
        return result[::-1]
    
class Puzzle:
    #Initialize the solution to the puzzle based on size N
    def __init__(self, N):
        self.N = N
        #tuples are faster to work with than 2-D arrays
        self.goal = tuple(list(range(1, N*N)) + [0])
        #Preparing for manhattan distance computations
        self.goalPosition = {
            val: (i // N, i % N) for i, val in enumerate(self.goal)
        }
    #Print the current state of the board
    def getBoard(self, state):
        for i in range(0, len(state), self.N):
            print(state[i:i+self.N])
        print()
    def reachGoal(self, state):
        return state == self.goal

    def misplacedTiles(self, state):
        return sum(1 for i in range(len(state)) if state[i] != 0 and state[i] != self.goal[i])
    
    def manhattanDistance(self, state):
        distance = 0
        for i, tile in enumerate(state):
            if tile == 0:
                continue
            # create coordinates
            row, column = i // self.N, i% self.N
            goalRow, goalColumn = self.goalPosition[tile]
            distance += abs(row - goalRow) + abs(column - goalColumn)
        return distance
    #generate successor states by moving the blank tile in all directions.
    def generateSuccessors(self, state):
        blankIndex = state.index(0)
        row, column = blankIndex // self.N, blankIndex % self.N
        successors = []
        # possible moves are up, down, left, right
        possibleMoves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for moveRow, moveColumn in possibleMoves:
            newRow, newColumn = row + moveRow, column + moveColumn
            if 0 <= newRow < self.N and 0 <= newColumn < self.N:
                newIndex = newRow * self.N + newColumn
                newState = list(state)
                newState[blankIndex], newState[newIndex] = newState[newIndex], newState[blankIndex]
                successors.append(tuple(newState))
        return successors

    def uniformCostSearch(self, start):
        # use a priority queue where priority is cost so far
        frontier = []
        heapq.heappush(frontier, Node(state=start, g=0, h=0))
        costs = {start: 0}

        while frontier:
            node = heapq.heappop(frontier)
            if node.g > costs.get(node.state, float("inf")):
                continue

            if self.goal == node.state:
                return node

            for successor in self.generateSuccessors(node.state):
                g_cost = node.g + 1
                if g_cost < costs.get(successor, float("inf")):
                    costs[successor] = g_cost
                    heapq.heappush(frontier, Node(state=successor, parent=node, g=g_cost, h=0))
        return None