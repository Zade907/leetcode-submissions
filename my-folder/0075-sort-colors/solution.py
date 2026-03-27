class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        right = len(nums) - 1
        parse = 0
        while parse<= right:
            if nums[parse] == 0:
                nums[parse], nums[left] = nums[left], nums[parse]
                parse += 1
                left += 1
            elif nums[parse] == 1:
                parse += 1
            else:
                nums[parse], nums[right] = nums[right], nums[parse]
                right -= 1
                
                
