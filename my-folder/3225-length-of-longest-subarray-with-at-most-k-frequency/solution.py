class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        n = len(nums)
        l,r = 0, 1
        freq[nums[l]] += 1
        maxLength = 1
        while r < n:
            freq[nums[r]] += 1
            if freq[nums[r]] <= k: #if condition satisfied just update the frequency and compare the currLen
                currLength = r - l + 1
                maxLength = max(currLength, maxLength)
            else: #freq of element is greater than k, freq[nums[r]] > k 
                while(freq[nums[r]] > k):
                    freq[nums[l]] -= 1 
                    l += 1
            r += 1
        return maxLength


