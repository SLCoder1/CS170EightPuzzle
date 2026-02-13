import time
import random
import csv
from tracemalloc import start
import matplotlib.pyplot as plt
from main import Puzzle

#Generate random states 
def randomState(N):
    array = list(range(N*N))
    while True:
        random.shuffle(array)
        tup=tuple(array)

        inversion = 0
        a = [x for x in tup if x != 0] 
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if a[i] > a[j]:
                    inversion += 1
        if inversion % 2 == 0: 
            return tup
# Run benchmarks to save into a cv file
def runTests(name, func, start):
    t0 = time.perf_counter()
    node = func(start)
    t1 = time.perf_counter()

    if node is None:
        return None, None
    path = node.g
    runtime = t1 - t0
    return path, runtime

p = Puzzle(3)
trials = 6
paths = []
uniformSearchSearchTimes = []
misplacedSearchTimes = []
manhattanSearchTimes = []

print("Running benchmarks")
#run trails
for i in range(trials):
    start = randomState(3)
    print("start: ")
    p.getBoard(start)
    #run tests
    d1, t1 = runTests(3, p.uniformCostSearch, start)
    d2, t2 = runTests(3, p.aStarMisplaced, start)
    d3, t3 = runTests(3, p.aStarManhattan, start)

    paths.append(d1)
    uniformSearchSearchTimes.append(t1)
    misplacedSearchTimes.append(t2)
    manhattanSearchTimes.append(t3)
    #save tests to a csv file
with open("benchmark.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["depth", "ucs", "misplaced", "manhattan"])
    for row in zip(paths, uniformSearchSearchTimes, misplacedSearchTimes, manhattanSearchTimes):
        writer.writerow(row)


#plotting data
plt.figure(figsize=(10, 5))
plt.plot(paths, uniformSearchSearchTimes, label="Uniform Cost Search", marker='o')
plt.plot(paths, misplacedSearchTimes, label="A* Misplaced Tiles", marker='o')
plt.plot(paths, manhattanSearchTimes, label="A* Manhattan Distance", marker='o')
plt.xlabel("Solution Depth")
plt.ylabel("Time (seconds)")
plt.title("Algorithm Performance on 8-Puzzle")
plt.legend()
plt.grid()
plt.savefig("benchmark.png")
plt.show()