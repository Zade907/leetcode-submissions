class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        oper = 0
        for i in nums:
            if(i%3==1):
                i -= 1 
                oper += 1 
            elif(i%3==2):
                i += 1
                oper += 1
            else:
                i=i
        return oper
            
