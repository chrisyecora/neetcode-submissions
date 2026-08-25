DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(q, visited):
            ROWS, COLS = len(grid), len(grid[0])
            minutes = 0
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in DIRECTIONS:
                        nr, nc = r + dr, c + dc
                        if (min(nr, nc) < 0 or nr == ROWS or nc == COLS or
                            (nr, nc) in visited or
                            grid[nr][nc] == 0 or grid[nr][nc] == 2):
                            continue
                    
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        visited.add((nr, nc))
                
                if q:
                    minutes += 1
            
            return max(0, minutes)

        visited = set()
        q = deque()
        minutes = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

        minutes = bfs(q, visited)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return minutes