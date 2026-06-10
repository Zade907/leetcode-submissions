class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowSum = 0
        left = 0
        minLen = float('inf')
        for right in range(len(nums)):
            windowSum += nums[right]
            while windowSum >= target:
                minLen = min(right - left + 1, minLen)
                windowSum -= nums[left]
                left += 1
        return minLen if minLen != float('inf') else 0 
