from main import Puzzle
from main import Node
import heapq

if __name__ == "__main__":

    #test puzzles of size N

    for N in [2, 3, 4]:
        print(f"\nTesting PUzzle with N = {N}")
        p = Puzzle(N)
        print("solved board:")
        p.getBoard(p.goal)

    #test nodes
    print("\nTesting Nodes")
    n1 = Node(state=(1, 2, 3, 4), g = 2, h = 3)
    n2 = Node(state=(1, 2, 3, 4), g = 1, h = 1)
    n3 = Node(state=(1, 2, 3, 4), g = 4, h = 0)

    heap = []
    heapq.heappush(heap, n1)
    heapq.heappush(heap, n2)
    heapq.heappush(heap, n3)

    print("Nodes are popped in order of lowest f to greatest f:")
    while heap:
        node = heapq.heappop(heap)
        print("f = ", node.f)

    #test heuristic function
    print("\n testing heuristic functions")
    p = Puzzle(3)
    test = (1, 2, 3, 4, 0, 6, 7, 8, 5)
    print("misplaced: ", p.misplacedTiles(test))
    print("manhattan: ", p.manhattanDistance(test))

    #test expland
    print("\n testing creating successors function")
    
    for child in p.generateSuccessors(test):
        p.getBoard(child)

    print("is goal: ", p.reachGoal(p.goal))