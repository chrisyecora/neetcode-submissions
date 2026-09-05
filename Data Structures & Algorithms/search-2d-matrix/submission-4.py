class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1
        # find row by doing binary search
        row = None
        while top <= bottom:
            middle = ((bottom - top) // 2) + top
            currRow = matrix[middle]
            if currRow[0] <= target and currRow[COLS - 1] >= target:
                row = currRow
                break
            
            if currRow[0] > target:
                bottom = middle - 1
            elif currRow[0] < target:
                top = middle + 1
            else:
                # middle[0] == target
                return True
        
        if not row:
            return False
        
        # find cell by doing binary search inside row
        left, right = 0, COLS - 1
        while left <= right:
            middle = (right - left) // 2 + left
            if row[middle] < target:
                left = middle + 1
            elif row[middle] > target:
                right = middle - 1
            else:
                return True
        
        return False



