class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        if low >= 10000:
            return 0
        for i in range(low,high+1):
            i = str(i)
            n = len(i)
            if n % 2 != 0:
                continue
            first,second = 0, 0
            for j in range(n//2):
                first += int(i[j]) 
                second += int(i[n-j-1])
            if first == second:
                count += 1 
        return count           
            




