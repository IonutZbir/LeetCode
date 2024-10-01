from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.cur = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        rows = len(matrix)
        cols = len(matrix[0])
        
        self.cur[0][0] = self.matrix[0][0]
        
        for c in range(1, cols): 
            self.cur[0][c] = self.matrix[0][c] + self.cur[0][c - 1]
        
        for r in range(1, rows):
            self.cur[r][0] = self.matrix[r][0] + self.cur[r - 1][0]
        
        for r in range(1, rows):
            for c in range(1, cols):
                self.cur[r][c] = self.matrix[r][c] + self.cur[r][c - 1] + self.cur[r - 1][c] - self.cur[r - 1][c - 1]
        
        print(self.__str__())

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if len(self.matrix) == 1 and len(self.matrix[0]) == 1:
            return self.matrix[0][0]
        return self.cur[row2][col2] - (self.cur[row2][col1 - 1] + self.cur[row1 - 1][col2]) + self.cur[row1 - 1][col1 - 1]

    def __str__(self):
        return str(self.cur)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)