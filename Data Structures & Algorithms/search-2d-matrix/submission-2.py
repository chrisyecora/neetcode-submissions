class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1

        while top <= bottom:
            middle = top + (bottom - top) // 2
            if matrix[middle][0] > target:
                bottom = middle - 1
            elif matrix[middle][n - 1] < target:
                top = middle + 1
            else:
                l, r = 0, n - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if matrix[middle][mid] < target:
                        l = mid + 1
                    elif matrix[middle][mid] > target:
                        r = mid - 1
                    else:
                        return True
                return False
        return False
