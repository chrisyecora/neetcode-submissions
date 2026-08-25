from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        r, c = 0, 0

        if grid[r][c] == 0:
            q.append((r, c))
            visited.add((r, c))

        length = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
                for dr, dc in directions:
                    print("r + dr, c + dc", r + dr, c + dc)
                    if (min(r + dr, c + dc) < 0 or 
                        r + dr == ROWS or c + dc == COLS or 
                        grid[r + dr][c + dc] == 1 
                        or (r + dr, c + dc) in visited):
                        continue

                    if r + dr == ROWS - 1 and c + dc == COLS - 1:
                        return length + 1
                    
                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            length += 1

        return -1