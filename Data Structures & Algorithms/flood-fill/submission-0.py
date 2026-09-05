class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        OG_COLOR = image[sr][sc]
        visit = set()

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit or image[r][c] != OG_COLOR:
                return
            
            visit.add((r, c))
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image