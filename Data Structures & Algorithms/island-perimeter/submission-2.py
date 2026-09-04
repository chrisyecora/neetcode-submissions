class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque()
        perimeter = 0
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    visit.add((r, c))
                    q.append((r, c))
                    while q:
                        row, col = q.popleft()
                        currPerimeter = 0
                        for dr, dc in DIRECTIONS:
                            if (min(row + dr, col + dc) < 0 or 
                                row + dr >= ROWS or col + dc >= COLS or 
                                grid[row + dr][col + dc] == 0
                            ):
                                perimeter += 1
                                continue
                            if (row + dr, col + dc) not in visit:
                                visit.add((row + dr, col + dc))
                                q.append((row + dr, col + dc))
                        perimeter += currPerimeter
        return perimeter
