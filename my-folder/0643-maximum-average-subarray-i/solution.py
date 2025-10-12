class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[0:k])
        windowSum =  maxSum
        for i in range(k, len(nums)):
            windowSum += nums[i] - nums[i - k]
            if(windowSum > maxSum):
                maxSum = windowSum
        return maxSum/k
