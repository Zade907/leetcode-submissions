class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = nums
        for i in reversed(nums):
            ans.append(i)
        return ans 
