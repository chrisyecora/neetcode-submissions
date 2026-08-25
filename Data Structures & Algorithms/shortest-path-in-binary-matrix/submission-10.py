from collections import deque
DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = COLS = len(grid)
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
                for dr, dc in DIRECTIONS:
                    if not self._isValidDirection(grid, r + dr, c + dc, visited):
                        continue
                    
                    if r + dr == ROWS - 1 and c + dc == COLS - 1:
                        return length + 1
                    
                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            length += 1

        return -1


    def _isValidDirection(self, grid, r, c, visited):
        ROWS = COLS = len(grid)
        if (min(r, c) < 0 or r == ROWS or c == COLS or 
            grid[r][c] == 1 or (r, c) in visited):
            return False
        
        return True