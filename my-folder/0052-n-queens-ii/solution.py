class Solution:
    def backtracking(self,row,cols,n,grid,diag1,diag2):
        if row == n:
            self.count += 1
            return
        for col in range(n):
            if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                grid[row][col] = 1
                cols[col] = True
                diag1[row + col] = True
                diag2[row - col + n -1] = True
                self.backtracking(row+1, cols,n,grid,diag1,diag2)
                grid[row][col] = 0
                cols[col] = False
                diag1[row + col] = False
                diag2[row - col + n -1] = False
    def totalNQueens(self, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(n)]
        self.count = 0
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)
        self.backtracking(0,cols,n,grid,diag1,diag2)
        return self.count
    
    
