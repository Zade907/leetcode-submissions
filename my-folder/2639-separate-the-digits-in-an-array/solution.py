class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            curr = []
            while i > 0:
                curr.append(i%10)
                i = i // 10
            for i in curr[::-1]:
                ans.append(i) 
        return ans 
