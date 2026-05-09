class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ones = s.count("1")
        zeros = n - ones

        if ones == 0 or zeros == 0 or n < 3:
            return 0
        if ones > 1 and s[0] == "1" and s[n - 1] == "1":
            return min(ones - 2, zeros)
        return min(ones - 1, zeros)
