class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = mid = float('inf')
        if len(nums)<3:
            return False
        for i in range (len(nums)):
            if nums[i] <= small: 
                small = nums[i]
            elif nums[i] <= mid: mid = nums[i]
            else:
                return True 
                


        return False
        
