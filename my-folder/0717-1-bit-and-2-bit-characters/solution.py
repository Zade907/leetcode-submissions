class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n:
            if bits[i] == 1:
                if i == n - 2:
                    return False 
                i += 2
                
            else:
                i += 1 
        return True
