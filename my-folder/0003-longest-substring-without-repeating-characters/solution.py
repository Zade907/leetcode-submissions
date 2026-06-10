class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alphabet = []
        maxLen = 0
        left = 0
        if len(s) <= 1:
            return len(s)
        for right in range(len(s)):
            if s[right] not in alphabet:
                alphabet.append(s[right])
            else:
                maxLen = max(maxLen, right - left)
                while s[right] in alphabet:
                    alphabet.remove(alphabet[0])
                    left += 1
                alphabet.append(s[right])
        maxLen = max(right - left + 1, maxLen)
        return maxLen

