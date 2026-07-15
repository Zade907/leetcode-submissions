class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math 
        oddSum = n*n
        evenSum = n * (n + 1)
        
        result = math. gcd(oddSum, evenSum)
        return result
