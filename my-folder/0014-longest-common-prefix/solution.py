class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        commonStr = ""
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                commonStr += strs[0][i]
            else:
                return commonStr
        return commonStr
