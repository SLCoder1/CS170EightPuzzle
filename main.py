from itertools import count
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
    
class Puzzle:
    #Initialize the solution to the puzzle based on size N
    def __init__(self, N):
        self.N = N
        self.goal = [
            [i*N + j + 1 for j in range(N)] for i in range(N)
        ]
        self.goal[N-1][N-1] = 0
    #Print the current state of the board
    def getBoard(self, state):
        for i in range(0, len(state), self.N):
            print(state[i:i+self.N])
        print()
    
    