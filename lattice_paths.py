import time

start = time.time_ns()
n = 20
grid = [[1 for x in range(n + 1)] for y in range(n + 1)]
grid[0][0] = 0

for x in range(1, n + 1):
    for y in range(1, n + 1):
        grid[x][y] = grid[x - 1][y] + grid[x][y - 1]

print(f"Time taken: {time.time_ns() - start} ns")
print(grid[n][n])
