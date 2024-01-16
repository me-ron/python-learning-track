class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.pre=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for  i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                self.pre[i][j] = self.pre[i-1][j] + self.pre[i][j-1] - self.pre[i-1][j-1] + matrix[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x=self.pre[row1][col1]
        y=self.pre[row2+1][col2+1]
        return x+y-self.pre[row1][col2+1]-self.pre[row2+1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)