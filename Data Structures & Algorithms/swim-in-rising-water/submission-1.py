class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        # minHeap
        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], (0, 0)))

        path = {}
        while minHeap:
            cost, coordinate = heapq.heappop(minHeap)
            row, col = coordinate
            
            if coordinate in path:
                continue
            
            path[coordinate] = cost

            if grid[row][col] == grid[len(grid) - 1][len(grid) - 1]:
                break

            # finding neighbors
            if row + 1 < len(grid):
                cost_down = cost + grid[row + 1][col] - grid[row][col]
                if cost_down < 0: cost_down = 0
                heapq.heappush(minHeap, (cost_down, (row + 1, col)))

            if row - 1 >= 0:
                cost_up = cost + grid[row - 1][col] - grid[row][col]
                if cost_up < 0: cost_up = 0
                heapq.heappush(minHeap, (cost_up, (row - 1, col)))
            
            if col + 1 < len(grid):
                cost_right = cost + grid[row][col + 1] - grid[row][col]
                if cost_right < 0: cost_left = 0
                heapq.heappush(minHeap, (cost_right, (row, col + 1)))

            if col - 1 >= 0:
                cost_left = cost + grid[row][col - 1] - grid[row][col]
                if cost_left < 0: cost_left = 0
                heapq.heappush(minHeap, (cost_left, (row, col - 1)))

        return max(path.values())