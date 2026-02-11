from main import Puzzle
from main import Node
import heapq

if __name__ == "__main__":

    #test puzzles of size N

    for N in [2, 3, 4]:
        print(f"\nTesting PUzzle with N = {N}")
        p = Puzzle(N)
        print("solved board:")
        print(p.getBoard([x for row in p.goal for x in row]))

    #test nodes
    print("\nTesting Nodes")
    n1 = Node(state=[1, 2, 3, 4], g = 2, h = 3)
    n2 = Node(state=[1, 2, 3, 4], g = 1, h = 1)
    n3 = Node(state=[1, 2, 3, 4], g = 4, h = 0)

    heap = []
    heapq.heappush(heap, n1)
    heapq.heappush(heap, n2)
    heapq.heappush(heap, n3)

    print("Nodes are popped in order of lowest f to greatest f:")
    while heap:
        node = heapq.heappop(heap)
        print("f = ", node.f)