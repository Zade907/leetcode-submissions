class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = deque(piles)
        mine = 0 
        while piles:
            piles.popleft()
            piles.pop()
            mine += piles.pop()
        return mine
