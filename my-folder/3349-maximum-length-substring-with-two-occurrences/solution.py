class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        l,r = 0,0
        freq = defaultdict(int)
        maxLen = 2
        while r < n:
            
            freq[s[r]] += 1
            while freq[s[r]] > 2:
                freq[s[l]] -= 1
                l += 1
            r += 1
            currLen = r - l 
            maxLen = max(maxLen, currLen)
        return maxLen
