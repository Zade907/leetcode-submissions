class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(m + 1):
            dp[0][i] = i
        for i in range(n + 1):
            dp[i][0] = i
        for row in range(1,n+1):
            for col in range(1, m + 1):
                diagonal = dp[row-1][col - 1]
                if word2[row - 1] == word1[col - 1]:
                    dp[row][col] = diagonal
                    continue
                delete = dp[row][col - 1]
                substitute = dp[row - 1][col]
                dp[row][col] = min(diagonal + 1, delete + 1, substitute + 1)
        return dp[n][m]

