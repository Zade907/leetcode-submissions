class Solution:
    def isUgly(self, n: int) -> bool:
        for i in range(0,32):
            for j in range(0,32):
                for k in range(0,32):
                    if(n ==(2**i)*(3**j)*(5**k)):
                        return True

