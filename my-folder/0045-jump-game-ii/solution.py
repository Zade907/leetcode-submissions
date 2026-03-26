class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        furthest = 0 
        curEnd = 0 
        jumps = 0
        for i in range(n -1):
            furthest = max(furthest, i + nums[i])
            if i == curEnd: 
                curEnd = furthest
                jumps += 1
        return jumps
                    
