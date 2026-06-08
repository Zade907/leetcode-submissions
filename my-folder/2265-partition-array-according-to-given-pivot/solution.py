class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
            left = []
            right= []
            numPivots = 0
            for i in nums:
                if i < pivot:
                    left.append(i)
                elif i > pivot:
                    right.append(i)
                else:
                    numPivots += 1
            return left + [pivot for i in range(numPivots)] + right
