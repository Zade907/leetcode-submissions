import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        currMax = 0
        n = len(nums)
        gcd = [0]* n
        for i in range(n):
            currMax = max(currMax, nums[i])
            gcd[i] = math.gcd(nums[i], currMax)
        gcd.sort()
        left = 0 
        right = n - 1
        result = 0 
        while left < right:
            result += math.gcd(gcd[left], gcd[right])
            left += 1 
            right -= 1
        return result 
            
