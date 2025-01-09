class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1 = []
        for i in range(n):
            l1.append(nums[i])
            l1.append(nums[i+n])
        return l1
