class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        i = None
        for j in range(len(nums)):
            if nums[j] == 1:
                if i is not None and j - i <= k: 
                    return False
                i = j
        return True


            


