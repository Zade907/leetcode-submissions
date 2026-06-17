class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        len_after = [0]*(n + 1) 
        for i,ch in enumerate(s):
            if 'a' <= ch and ch <= 'z':
                len_after[i + 1] = len_after[i] + 1
            elif ch == '*':
                len_after[i + 1] = max(0,len_after[i] - 1)
            elif ch == "#":
                len_after[i + 1] = len_after[i]*2
            else:
                len_after[i + 1] = len_after[i]
        
        if k >= len_after[n]: 
            return '.'


        for i in range(n - 1, -1, -1):
            c = s[i]
            prev_len = len_after[i]

            if c == '*':
                continue
            elif c == '#':
                if prev_len > 0:
                    k %= prev_len
            elif c == "%":
                k = prev_len - 1 - k
            else:
                if k == prev_len:
                    return c
        return '.'
