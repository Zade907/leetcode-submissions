class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = 0
        while i < len(s) and s[i] == "1":
            i+= 1
        for j in range(i,len(s)):
            if s[j] == "1":
                return False
        return True
