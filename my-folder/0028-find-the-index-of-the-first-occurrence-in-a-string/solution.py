class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0 
        n = len(needle)
        for i,j in enumerate(haystack):
            if j == needle[0]:
                if i + n <= len(haystack) and haystack[i:i + n] == needle:
                    return i
        return -1

