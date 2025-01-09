class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        numb = 0
        for i in stones:
            if i in jewels:
                numb+=1
        return numb
