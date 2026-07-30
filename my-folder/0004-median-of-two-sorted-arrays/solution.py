class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        # if m == 0:
        #     median = n//2
        #     return nums2[median] if n % 2 != 0 else (nums2[median - 1] + nums2[median])/2
        # if n == 0:
        #     median = m//2 
        #     return nums1[median] if m % 2 != 0 else (nums1[median - 1] + nums1[median])/2
        medianIndex = (m + n)//2 + 1
        totalNumbers = m + n
        prev, curr = 0, 0
        nums1Index = 0
        nums2Index = 0
        print(medianIndex)
        for i in range(medianIndex):
            prev = curr
            
            if nums2Index == n :
                curr = nums1[nums1Index]
                nums1Index += 1
            elif nums1Index == m:
                curr = nums2[nums2Index]
                nums2Index += 1
            elif nums1[nums1Index] < nums2[nums2Index]:
                curr = nums1[nums1Index]
                nums1Index += 1
            else:
                curr = nums2[nums2Index]
                nums2Index += 1
        return curr if totalNumbers % 2 != 0 else ((prev + curr)/2)
