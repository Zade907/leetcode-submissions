class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        index = {0: [], 1: [], 2: []}
        for i,j in enumerate(nums):
            index[j].append(i)
        absDiff = float("inf")
        for i in index[1]:
            for j in index[2]:
                absDiff = min(absDiff, abs(i - j))
        return -1 if absDiff == float("inf") else absDiff
