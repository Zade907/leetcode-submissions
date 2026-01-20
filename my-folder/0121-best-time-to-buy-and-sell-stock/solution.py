class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        # highest = 0 
        for i in prices:
            if i < lowest:
                lowest = i 
            #     highest = 0
            # if i > highest:
            #     highest = i
            if profit < i - lowest:
                profit = i - lowest
        return profit
