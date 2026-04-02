class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        
        NEG = float('-inf')
        dp = [[[NEG for _ in range(3)] for _ in range(n)] for _ in range(m)]
        
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                    
                coin = coins[i][j]
                
                for k in range(3):
                    best = NEG
                    
                    if i > 0:
                        best = max(best, dp[i - 1][j][k])
                    if j > 0:
                        best = max(best, dp[i][j - 1][k])
                    
                    dp[i][j][k] = best + coin
            
                if coin < 0:
                    for k in range(1,3):
                        best = NEG
                        if i > 0:
                            best = max(best, dp[i - 1][j][k - 1])
                        if j > 0:
                            best = max(best, dp[i][j - 1][k - 1])
                        
                        dp[i][j][k] = max(dp[i][j][k], best)

        return max(dp[m-1][n-1])
