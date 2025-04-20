import heapq
import time

# Grid kota:
# R: Restoran (start)
# C: Customer (goal)
# .: Jalan biasa
# #: Rintangan (jalan tertutup)

grid3 = [
    ['R', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', 'C']
]

def manhattan(a, b):
    """Heuristik jarak Manhattan."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_pos(grid, symbol):
    """Cari posisi simbol (R atau C) di grid."""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == symbol:
                return (i, j)
    return None

def a_star_grid(grid, start, goal):
    """Implementasi A* pada grid dengan rintangan."""
    open_set = []
    heapq.heappush(open_set, (0 + manhattan(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path, g, len(visited)
        if current in visited:
            continue
        visited.add(current)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = current[0] + dx, current[1] + dy
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                if grid[ni][nj] != '#' and (ni, nj) not in visited:
                    new_cost = g + 1  # Bobot jalan (bisa ditambah fitur: kemacetan dll)
                    priority = new_cost + manhattan((ni, nj), goal)
                    heapq.heappush(open_set, (priority, new_cost, (ni, nj), path + [(ni, nj)]))
    return None, float('inf'), len(visited)

# Jalankan A*
start = find_pos(grid3, 'R')
goal = find_pos(grid3, 'C')

start_time = time.time()
path, cost, nodes = a_star_grid(grid3, start, goal)
time_taken = (time.time() - start_time) * 1000  # dalam milidetik

# Output
print("A* Delivery Path:", path)
print("Total cost (steps):", cost)
print("Execution time (ms):", round(time_taken, 2))
print("Visited nodes:", nodes)
