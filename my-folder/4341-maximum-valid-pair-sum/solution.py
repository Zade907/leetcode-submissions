class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        maxExplored = 0
        leftMax = nums[maxExplored]
        n = len(nums)
        currMax = leftMax + nums[k]
        for i in range(k + 1,n):
            maxExplored += 1
            leftMax = max(leftMax, nums[maxExplored])
            newSum = nums[i] + leftMax
            currMax = max(newSum, currMax)
        return currMax
            
            
            
