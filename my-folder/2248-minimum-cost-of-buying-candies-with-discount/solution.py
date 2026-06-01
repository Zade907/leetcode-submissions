class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        i = n - 1
        if n < 3:
            return sum(cost)
        cost.sort()
        res = 0
        while i >= 2:
            res += cost[i] + cost[i - 1]
            i = i - 3
        return res + sum(cost[0:i + 1])


