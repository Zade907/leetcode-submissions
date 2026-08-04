class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l = min(nums)
        r = max(nums)
        res = []
        for i in range(l,r + 1):
            if i not in nums:
                res.append(i)
        return res
