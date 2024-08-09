
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float('inf')
        
        for num in nums:
            # Check if the current number is closer to zero than the closest found so far.
            # If it is closer or if it is equally close but positive, update closest.
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num
        
        return closest

