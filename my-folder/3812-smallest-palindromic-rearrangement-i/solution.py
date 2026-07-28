class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        freq = Counter(s[:n//2])
        mid = s[n//2] if n % 2 != 0 else ""
        half = "".join(c * freq[c] for c in ascii_lowercase)
        return half + mid + half[::-1]
