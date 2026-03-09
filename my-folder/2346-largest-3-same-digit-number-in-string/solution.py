class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i,j,k = 0,1,2
        maximum = "0"
        while k < len(num):
            if num[i] == num[j] == num[k]:
                currNum = num[i] + num[j] + num[k]
                if int(currNum) >= int(maximum):
                    maximum = currNum
            i += 1
            j += 1 
            k += 1
        return str(maximum) if maximum != "0" else ""
