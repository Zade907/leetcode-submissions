class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        dist = float("inf")
        for i,j in enumerate(nums):
            if j == target:
                dist = min(dist,abs(i - start))
        return dist
