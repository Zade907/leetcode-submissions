class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        list1 = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(i!=j and nums[i]==nums[j]):
                    list1.append(nums[j])
        return list1
