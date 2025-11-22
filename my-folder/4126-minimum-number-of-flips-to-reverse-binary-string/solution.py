class Solution:
    def minimumFlips(self, n: int) -> int:
            s = bin(n)[2:]
            reverse = str(s)[::-1]
            counter = 0
            for i in range(len(s)):
                if s[i] != reverse[i]:
                    counter += 1
            return counter
