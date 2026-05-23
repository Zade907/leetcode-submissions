class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                flag += 1 
        return flag <= 1
