class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixSum = [0]*n
        leftSum = 0
        for i in range(n):
            prefixSum[i] = leftSum
            leftSum += nums[i]
        suffixSum = [0]*n
        rightSum = 0
        for i in range(n-1,-1,-1):
            suffixSum[i] = rightSum 
            rightSum += nums[i]
        return [abs(prefixSum[i]- suffixSum[i]) for i in range(n)]
