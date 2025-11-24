class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        prefix = 0
        for i in nums:
            prefix = prefix*2 + i 
            answer.append(True if prefix%5 == 0 else False)
        return answer
