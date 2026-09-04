class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [[1,0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    q.append((r, c))
                    visit.add((r, c))
                    while q:
                        row, col = q.popleft()
                        for dr, dc in DIRECTIONS:
                            if (min(row + dr, col + dc) < 0 or 
                                row + dr >= ROWS or col + dc >= COLS or 
                                (row + dr, col + dc) in visit or 
                                grid[row + dr][col + dc] == "0"):
                                continue
                            visit.add((row + dr, col + dc))
                            q.append((row + dr, col + dc))
                    islands += 1

        return islands
