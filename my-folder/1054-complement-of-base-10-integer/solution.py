class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: 
            return 1 
        count = 0
        temp_n = n
        while temp_n > 0:
            count += 1
            temp_n = temp_n//2
        maxNumber = (2 ** count) - 1
        return maxNumber - n


