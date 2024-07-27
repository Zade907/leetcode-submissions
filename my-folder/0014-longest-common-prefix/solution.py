class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        x = sorted(strs)
        temp1 = x[0]
        temp2 = x[-1]
        for i in range(min(len(temp1),len(temp2))):
            if(temp1[i]!=temp2[i]):
                return common_prefix
            common_prefix += temp1[i]
        return common_prefix
        
