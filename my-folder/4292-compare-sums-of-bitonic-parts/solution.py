class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        prevElem = nums[0]
        currMaxIndex = 0
        for i,j in enumerate(nums[1:]):
            if j > prevElem:
                print(i,j)
                prevElem = j
                currMaxIndex = i + 1
            else:
                break
        ascSum = sum(nums[:currMaxIndex + 1])
        descSum = sum(nums[currMaxIndex: len(nums) + 1])
        if ascSum > descSum:
            return 0
        elif ascSum < descSum:
            return 1
        else:
            return -1
                
            
