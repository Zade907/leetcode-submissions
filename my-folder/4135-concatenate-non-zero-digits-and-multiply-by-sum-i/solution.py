class Solution:
    def sumAndMultiply(self, n: int) -> int:
        cleaned = "".join([i for i in str(n) if i != "0"])
        sum = 0
        if not cleaned:
            return 0

        for i in cleaned:
            sum += int(i) 
        return int(cleaned) * sum 
