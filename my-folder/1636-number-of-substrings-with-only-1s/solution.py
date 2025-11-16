class Solution:
    def numSub(self, s: str) -> int:
        n = 0
        substring = 0
        mod = 1e9+7
        for i in range(len(s)):
            if s[i] == "1":
                n += 1
                if i != len(s) - 1:
                    continue
            substring += (n*(n+1))//2
            n = 0
        return int(substring%mod)

