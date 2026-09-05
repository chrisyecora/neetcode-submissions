class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # store each row and col in a hashmap
        rows = defaultdict(int)
        cols = defaultdict(int)

        # assign servers to rows/cols
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        

        ans = 0
        # check which rows/cols > 1 server? ans += row/col : 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (rows[r] > 1 or cols[c] > 1):
                    ans += 1
                
        
        return ans