class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1 
        votes = 0

        for i in nums:
            if votes == 0:
                candidate = i
                votes = 1
            else:
                if i == candidate:
                    votes += 1 
                else:
                    votes -= 1 
        
        count = 0 

        for i in nums:
            if i == candidate:
                count += 1 
        
        if count > len(nums)//2:
            return candidate
        else:
            return -1
