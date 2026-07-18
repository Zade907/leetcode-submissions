class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n <= 1:
            return s 
        quotient = n // 2 
        increase = m * quotient
        return s + increase - (quotient - 1)
