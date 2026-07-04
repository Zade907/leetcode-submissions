class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        freq = Counter(nums)
        if freq[nums[len(nums)//2]] == 1: return True
        else: return False
