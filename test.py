from main import Puzzle
import time


def run(name, func, puzzle, start):
    t0 = time.time()
    goal, expanded, maxq = func(start)
    t1 = time.time()

    if goal is None:
        print(name, "→ No solution")
        return

    print(name)
    print("Depth:", goal.g)
    print("Expanded:", expanded)
    print("Max queue:", maxq)
    print("Time:", round(t1 - t0, 4), "sec")
    print()


if __name__ == "__main__":

    N = int(input("Enter puzzle size N: "))

    print("Enter board row by row, use 0 for blank. A row should include spaces between each number, and press enter after each row")

    values = []
    for _ in range(N):
        values.extend(map(int, input().split()))

    start = tuple(values)

    p = Puzzle(N)

    if not p.isSolvable(start):
        print("Unsolvable puzzle")
        exit()

    print("\nInitial state:")
    p.getBoard(start)

    print("Goal:")
    p.getBoard(p.goal)

    print("\nRunning algorithms...\n")

    run("Uniform Cost", p.uniformCostSearch, p, start)
    run("A* Misplaced", p.aStarMisplaced, p, start)
    run("A* Manhattan", p.aStarManhattan, p, start)

    goal, _, _ = p.aStarManhattan(start)

    print("Solution path:\n")
    for s in goal.path():
        p.getBoard(s)
