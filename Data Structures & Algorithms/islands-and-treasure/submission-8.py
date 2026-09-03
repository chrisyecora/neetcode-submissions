class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()
        visit = set()   

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        while q:
            r, c, distance = q.popleft()
            visit.add((r, c))
            for dr, dc in DIRECTIONS:
                if r + dr < 0 or c + dc < 0 or r + dr > ROWS - 1 or c + dc > COLS - 1:
                    continue
                else:
                    if grid[r + dr][c + dc] == 2147483647:
                        grid[r + dr][c + dc] = distance + 1
                        q.append((r + dr, c + dc, distance + 1))        