class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        balance = 0
        prefixXor = 0
        visited = {(0,0): -1}
        longest = 0
        for i,x in enumerate(nums):
            prefixXor ^= x
            
            balance += 1 if x%2 == 0 else -1
            key = (prefixXor,balance)
            
            if key in visited:
                longest = max(longest, i - visited[key] )
                
            else:
                visited[key] = i
        return longest
