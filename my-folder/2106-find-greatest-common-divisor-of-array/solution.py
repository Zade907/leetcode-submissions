class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def eucledianAlgorithm(a,b):
            while b != 0:
                remainder = a % b
                a = b 
                b = remainder
            return a
        
        currentMin = min(nums[0],nums[1])
        currentMax = max(nums[0],nums[1])
        for i in nums[2:]:
            if i < currentMin:
                currentMin = i
            elif i > currentMax: currentMax = i

        return eucledianAlgorithm(currentMax, currentMin)

