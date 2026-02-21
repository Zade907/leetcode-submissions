class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = [[n1,n2] for n1,n2 in zip(speed,efficiency)]
        pairs = sorted(pairs, key = lambda p : p[1], reverse  = True)
        minHeap = []
        
        n1Sum = 0
        maxPerformance = 0

        for n1,n2 in pairs:
            heapq.heappush(minHeap,n1)
            n1Sum += n1
            if len(minHeap) > k:
                small = heapq.heappop(minHeap)
                n1Sum -= small
            
            maxPerformance = max(maxPerformance,n1Sum * n2)
            
            
        return maxPerformance % (10**9 + 7)
