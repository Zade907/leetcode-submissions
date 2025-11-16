class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        zero = 1
        maximum = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zero -= 1
            if zero != -1:
                maximum = max(maximum,j-i)
            while zero < 0:
                if nums[i] == 0:
                    zero += 1
                i += 1
        return maximum     



