from collections import deque

def numIslands(grid):
    if not grid:
        return 0

    height = len(grid)
    length = len(grid[0])
    seen = set()
    count = 0

    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up

    for j in range(height):
        for i in range(length):
            if grid[j][i] == "1" and (j,i) not in seen:
                count += 1
                queue = deque()
                queue.append((j,i))
                seen.add((j,i))
                while queue:
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < height and 0 <= nc < length:
                            if grid[nr][nc] == "1" and (nr,nc) not in seen:
                                queue.append((nr,nc))
                                seen.add((nr,nc))
    return count

# grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
# ]

grid = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]]
print(numIslands(grid))