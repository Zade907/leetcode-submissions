class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 1
        while i < len(nums) and nums[i-1] < nums[i]:
            i += 1
        if i == 1 or i == len(nums):
            return False
        while i < len(nums) and nums[i-1] > nums[i]:
            i += 1
        if i == len(nums):
            return False
        while i < len(nums) and nums[i-1] < nums[i]:
            i += 1
        return i == len(nums)



