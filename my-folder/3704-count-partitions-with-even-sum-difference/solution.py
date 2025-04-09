class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range (n-1):
            if(sum(nums[:i])%2==0 and sum(nums[i:n])%2==0 or sum(nums[:i])%2!=0 and sum (nums[i:n])%2!=0):
                count += 1
        return count
 
