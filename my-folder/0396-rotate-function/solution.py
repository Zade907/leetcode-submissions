class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        defaultSum = sum(nums)
        k = len(nums) - 1
        rotatedSum = 0
        temp = 0
        for i in nums:
            rotatedSum += i * temp
            temp += 1
        maxSum = rotatedSum

        for i in reversed(nums):
            currSum = rotatedSum - (i * k)
            currSum += (defaultSum - i)
            maxSum = max(currSum,maxSum)
            rotatedSum = currSum
        return maxSum
