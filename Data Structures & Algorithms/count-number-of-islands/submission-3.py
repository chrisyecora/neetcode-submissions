class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid: List[List[str]], r: int, c: int, visited: set) -> int:
            ROWS, COLS = len(grid), len(grid[0])
            # goal: build out the island
            # base case:
                 # 1. out of bounds
                 # 2. hit a 0 -> end of island
                 # 3. already been here
            if min(r, c) < 0 or r == ROWS or c == COLS:
                return
            
            if grid[r][c] == "0":
                return

            if (r, c) in visited:
                return

            
            visited.add((r, c))
            dfs(grid, r, c - 1, visited)
            dfs(grid, r, c + 1, visited)
            dfs(grid, r - 1, c, visited)
            dfs(grid, r + 1, c, visited)

        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):  
                if grid[r][c] == "1":
                    #island!
                    if (r, c) not in visited:
                        # How far does it go? populate visited
                        dfs(grid, r, c, visited)
                        count += 1

        return count


