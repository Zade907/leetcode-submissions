class Solution:
    def backtracking(self,row,cols,n,grid,sols,diag1,diag2):
        if row == n:
            sol = ["".join(row) for row in grid]
            sols.append(sol)
            return
        for col in range(n):
            if grid[row][col] == "." and cols[col] == False and not diag1[col+ row] and not diag2[row - col + n - 1]:
                grid[row][col] = "Q"
                cols[col] = True
                diag1[row + col] = True
                diag2[row - col + n - 1] = True
                self.backtracking(row + 1,cols,n,grid,sols,diag1,diag2)
                grid[row][col] = "."
                cols[col] = False 
                diag1[row + col]= False
                diag2[row - col + n - 1] = False
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["." for _ in range(n)]for _ in range(n)]
        sols = []
        diag1 = [False]*(2*n - 1)
        diag2 = [False]*(2*n - 1)
        cols = [False]*n

        self.backtracking(0,cols,n,grid,sols,diag1,diag2)
        return sols
    
