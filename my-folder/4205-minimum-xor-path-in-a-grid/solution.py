class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                curr = set()
                if row > 0:
                    for i in dp[row - 1][col]:
                        curr.add(i ^ grid[row][col])
                if col > 0:
                    for j in dp[row][col - 1]:
                        curr.add(j ^ grid[row][col])
                dp[row][col] = curr
        return min(dp[m - 1][n - 1])
