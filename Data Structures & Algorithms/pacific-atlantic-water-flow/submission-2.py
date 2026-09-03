class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        reachedPacific = set()
        reachedAtlantic = set()
        def dfs(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                (r, c) in visit or heights[r][c] < prevHeight
                ):
                return
            
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])


        for c in range(COLS):
            dfs(0, c, reachedPacific, heights[0][c])
            dfs(ROWS - 1, c, reachedAtlantic, heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r, 0, reachedPacific, heights[r][0])
            dfs(r, COLS - 1, reachedAtlantic, heights[r][COLS - 1])

        ans = []
        for coord in reachedPacific:
            if coord in reachedAtlantic:
                ans.append([coord[0], coord[1]])
        
        return ans