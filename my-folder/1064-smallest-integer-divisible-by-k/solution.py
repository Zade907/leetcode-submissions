class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0 : return -1
        n = 1 % k
        # MOD = 10**9 + 7
        size = 1
        while True:
            if n == 0:
                # n = n % MOD
                return size
                break
            n = (n * 10 + 1) % k
            size += 1 

