class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # returns: size (int) of the island
        def dfs(grid, r, c, visited) -> int:
            ROWS, COLS = len(grid), len(grid[0])
            if (min(r, c) < 0 or 
                r == ROWS or 
                c == COLS or
                (r, c) in visited or
                grid[r][c] == 0):
                return 0

            visited.add((r, c))
            return (1 + 
                dfs(grid, r, c + 1, visited) + 
                dfs(grid, r, c - 1, visited) + 
                dfs(grid, r - 1, c, visited) + 
                dfs(grid, r + 1, c, visited)
            )


        visited = set()
        max_size = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_size = max(max_size, dfs(grid, r, c, visited))
            
        return max_size
        

        