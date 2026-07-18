class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        cat = [0] * n
        for i,x in enumerate(nums):
            if x < a:
                cat[i] = 0
            elif x > b:
                cat[i] = 2 
            else:
                cat[i] = 1
        currentSeenCat = [0,0,0]
        totalSwap = 0 

        for c in cat:
            for higherCat in range(c + 1, 3):
                totalSwap += currentSeenCat[higherCat]
            currentSeenCat[c] += 1
        return totalSwap % MOD
        
        
