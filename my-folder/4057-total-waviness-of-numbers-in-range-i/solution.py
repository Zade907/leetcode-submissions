class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        counter = 0
        for i in range(num1,num2+1):
            s = str(i)
            for j in range(1,len(s)-1):
                if((s[j-1] < s[j] and s[j+1] < s[j]) or(s[j-1] > s[j] and s[j+1] > s[j])):
                    counter += 1

        return counter
