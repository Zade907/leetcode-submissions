class Solution:
    def countKConstraintSubstrings(self, s: str, t: int) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            zero_count, one_count = 0, 0
            for j in range(i, n):
                if s[j] == '0':
                    zero_count += 1
                else:
                    one_count += 1
                
                if zero_count <= t or one_count <= t:
                    ans += 1

        return ans
