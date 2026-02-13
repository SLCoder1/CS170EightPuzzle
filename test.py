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

    # test heuristic function on a non-trivial state
    print("\n testing heuristic functions")
    p = Puzzle(3)
    test = (1, 2, 3, 4, 0, 6, 7, 8, 5)  # one tile displaced from goal
    print("state for heuristics:")
    p.getBoard(test)
    print("misplaced: ", p.misplacedTiles(test))
    print("manhattan: ", p.manhattanDistance(test))

    # test expand
    print("\n testing creating successors function")
    for child in p.generateSuccessors(test):
        p.getBoard(child)

    print("is goal: ", p.reachGoal(p.goal))

    # testing uniform cost search
    print("\n testing uniform cost search")
    p = Puzzle(3)

    # a simple one-move solvable configuration
    solvable = (1, 2, 3, 4, 5, 6, 7, 0, 8)
    print("solvable start state:")
    p.getBoard(solvable)
    result = p.uniformCostSearch(solvable)
    if result is None:
        print("ERROR: expected a solution but none was found")
    else:
        print("found path length", len(result.path()) - 1)

    # a known unsolvable configuration (parity mismatch)
    unsolvable = (1, 2, 3, 4, 0, 6, 7, 8, 5)
    print("unsolvable start state:")
    p.getBoard(unsolvable)
    result = p.uniformCostSearch(unsolvable)
    if result is None:
        print("correctly reports no solution")
    else:
        print("WARNING: found path for unsolvable state")
        for s in result.path():
            p.getBoard(s)

    # try several random solvable states to make sure solver works reliably
    import random

    def is_solvable(state, N=3):
        inv = 0
        arr = [x for x in state if x != 0]
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    inv += 1
        return inv % 2 == 0

    solvable = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    print("solvable start state:")
    p.getBoard(solvable)
    result = p.uniformCostSearch(solvable)
    if result is None:
        print("ERROR: expected a solution but none was found")
    else:
        print("found path length", len(result.path()) - 1)

    solvable = (1, 2, 3, 5, 0, 6, 4, 7, 8)
    print("solvable start state:")
    p.getBoard(solvable)
    result = p.uniformCostSearch(solvable)
    if result is None:
        print("ERROR: expected a solution but none was found")
    else:
        print("found path length", len(result.path()) - 1)

    solvable = (1, 3, 6, 5, 0, 2, 4, 7, 8)
    print("solvable start state:")
    p.getBoard(solvable)
    result = p.uniformCostSearch(solvable)
    if result is None:
        print("ERROR: expected a solution but none was found")
    else:
        print("found path length", len(result.path()) - 1)

    solvable = (1, 3, 6, 5, 0, 7, 4, 8, 2)
    print("solvable start state:")
    p.getBoard(solvable)
    result = p.uniformCostSearch(solvable)
    if result is None:
        print("ERROR: expected a solution but none was found")
    else:
        print("found path length", len(result.path()) - 1)
    
    solvable = (1, 6, 7, 5, 0, 3, 4, 8, 2)
    print("solvable start state:")
    p.getBoard(solvable)
    result = p.uniformCostSearch(solvable)
    if result is None:
        print("ERROR: expected a solution but none was found")
    else:
        print("found path length", len(result.path()) - 1)

    solvable = (7, 1, 2, 4, 8, 5, 6, 3, 0)
    print("solvable start state:")
    p.getBoard(solvable)
    result = p.uniformCostSearch(solvable)
    if result is None:
        print("ERROR: expected a solution but none was found")
    else:
        print("found path length", len(result.path()) - 1)

    solvable = (0, 7, 2, 4, 6, 1, 3, 5, 8)
    print("solvable start state:")
    p.getBoard(solvable)
    result = p.uniformCostSearch(solvable)
    if result is None:
        print("ERROR: expected a solution but none was found")
    else:
        print("found path length", len(result.path()) - 1)