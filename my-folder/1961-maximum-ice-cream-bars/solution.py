class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0 
        currSpent = 0
        for cost in costs:
            currSpent += cost
            if currSpent <= coins:
                count += 1 
            else:
                break
        return count 
    
