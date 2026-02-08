class Solution:
    def tribonacci(self, n: int) -> int:
        f = [0]*n
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n ==2:
            return 1
        f[1],f[2] = 1,1
        for i in range(n):
            if i + 3 <= n - 1:
                f[i + 3] = f[i] + f[i+ 2] + f[i + 1]
        
        return sum(f[n-3:n])


