class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        lowestPrice = prices[0]
        for i in range(n):
            if(prices[i]<lowestPrice):
                lowestPrice = prices[i]
            if(prices[i]-lowestPrice > profit):
                profit = prices[i]-lowestPrice
        return profit
