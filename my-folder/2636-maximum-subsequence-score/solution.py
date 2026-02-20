class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1,n2) for n1,n2 in zip(nums1,nums2)]
        pairs = sorted(pairs, key = lambda p : p[1], reverse = True)

        nSum = 0
        maxScore = 0
        minHeap = []
        for n1,n2 in pairs:
            nSum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k:
                nPop = heapq.heappop(minHeap)
                nSum -= nPop
            if len(minHeap) == k:
                maxScore = max(maxScore, nSum * n2)
        return maxScore


