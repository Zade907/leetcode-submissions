class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        one = abs(z - x)
        two = abs(z -y)
        if one < two: 
            return 1
        elif two < one:
            return 2
        else:
            return 0
            
