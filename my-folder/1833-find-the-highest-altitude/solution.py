class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxHeight = 0 
        currHeight = 0
        for i in gain:
            currHeight += i
            maxHeight = max(maxHeight, currHeight)
        return maxHeight
        
