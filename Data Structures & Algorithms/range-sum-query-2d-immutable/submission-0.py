class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for i in range(len(matrix)):
            total = 0
            row = []
            for j in range(len(matrix[i])):
                total += matrix[i][j]
                row.append(total)
            self.prefix.append(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            preRight = self.prefix[i][col2]
            preLeft = self.prefix[i][col1 - 1] if col1 > 0 else 0
            total += (preRight - preLeft)
        
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)