class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            curr = 0
            while i >= 10:
                curr += i % 10
                i = i//10
            curr += i
            res.append(curr)
        return min(res)
