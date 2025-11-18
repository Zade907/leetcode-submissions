class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        answer = [0]*len(nums)
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for j in range(len(nums)-1,-1,-1):
            answer[j] = answer[j] * suffix
            suffix *= nums[j]
        return answer
