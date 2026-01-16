class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) 
        i = 0
        while i < j:
            if nums[j - 1] == val:
                j -= 1
                continue
            if nums[i] == val:
                nums[i] = nums[j - 1]
                nums[j - 1] = val
                j -= 1
            i += 1
        return j 

        

    
