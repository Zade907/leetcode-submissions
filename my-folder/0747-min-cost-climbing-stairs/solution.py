class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = cost[0] 
        mid = cost[1]

        for i in cost[2:]:
            curr = i + min(prev, mid)
            prev = mid
            mid = curr 
        return min(prev,mid)
