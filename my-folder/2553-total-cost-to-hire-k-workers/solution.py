class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        leftHeap = costs[:candidates]
        heapq.heapify(leftHeap)

        rightHeap = costs[max(candidates, n - candidates):] 
        heapq.heapify(rightHeap)

        leftPointer = candidates
        rightPointer = n - candidates - 1
        totalCost = 0

        for i in range(k):
            
            if not rightHeap or (leftHeap and (leftHeap[0] <= rightHeap[0])):
                totalCost += heapq.heappop(leftHeap)
                if leftPointer <= rightPointer:
                    heapq.heappush(leftHeap, costs[leftPointer])
                    leftPointer += 1

            else:
                totalCost += heapq.heappop(rightHeap)
                if leftPointer <= rightPointer:
                    heapq.heappush(rightHeap, costs[rightPointer])
                    rightPointer -= 1

        return totalCost
