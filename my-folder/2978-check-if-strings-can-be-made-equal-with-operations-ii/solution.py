class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1Even = {}
        s1Odd = {}
        for i,j in enumerate(s1):
            if i % 2 == 0:
                if j in s1Even:
                    s1Even[j] += 1
                else:
                    s1Even[j] = 1
            else:
                if j in s1Odd:
                    s1Odd[j] += 1
                else:
                    s1Odd[j] = 1
        for i,j in enumerate(s2):
            if i % 2 == 0:
                if j in s1Even and s1Even[j] > 0:
                    s1Even[j] -= 1
                else:
                    return False
            else:
                if j in s1Odd and s1Odd[j] > 0:
                    s1Odd[j] -= 1
                else:
                    return False
        return True
