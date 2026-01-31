class Solution:
    def minimumK(self, nums: List[int]) -> int:
        l, r = 1, max(nums) + len(nums)

        while l < r:
            k = (l + r) // 2
            temp_k = sum((x + k - 1) // k for x in nums)

            if temp_k <= k * k:
                r = k
            else:
                l = k + 1

        return l

        
