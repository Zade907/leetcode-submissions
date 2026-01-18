class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,1 
        while r < len(nums):
            while r + 1 < len(nums) and nums[r] == nums[r-1]:
                r += 1
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1

