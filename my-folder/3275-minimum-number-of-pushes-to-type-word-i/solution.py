class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        cost = 0
        for i in range(4):
            if n > 0:
                cost += n 
                n -= 8
            else:
                break
        return cost

