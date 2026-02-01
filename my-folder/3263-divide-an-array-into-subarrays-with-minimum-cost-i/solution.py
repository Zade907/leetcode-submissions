class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        second = float('inf')
        third = float('inf')
        if len(nums) == 3:
            return sum(nums)
        for i in nums[1:]:
            if i < second:
                third = second 
                second = i
            elif i < third:
                third = i
        return nums[0] + second + third
