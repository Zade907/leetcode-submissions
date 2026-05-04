class Solution:
    def sumOfPrimesInRange(self, m: int) -> int:
        n = int(str(m)[::-1])
        if m > n:
            m,n = n,m
        def primeCheck(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        total = 0
        for i in range(m, n + 1):
            if primeCheck(i):
                total += i
        return total


