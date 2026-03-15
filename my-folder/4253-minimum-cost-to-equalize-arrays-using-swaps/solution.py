class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        count1= Counter(nums1)
        count2 = Counter(nums2)
        union = list(set(nums1) | set(nums2))
        oper = 0
        for i in union:
            if (count1[i] + count2[i]) % 2 == 1:
                return -1
            diff = abs(count1[i] - count2[i])
            oper += diff/4
        return int(oper)

        
