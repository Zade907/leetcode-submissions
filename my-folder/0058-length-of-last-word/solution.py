class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        finalCount = 0
        count = 0
        i = 0
        while i < len(s):
            while i < len(s) and s[i] != " ":
                i+= 1
                count += 1
            else:
                finalCount = count
            if i < len(s) and s[i] == " ":
                i += 1
                count = 0
        return count 
