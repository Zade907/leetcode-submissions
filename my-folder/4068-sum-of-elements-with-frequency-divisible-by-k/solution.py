class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        dict1 = {}
        sum = 0
        old = 0
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1

        for key in dict1:
            if(dict1[key] % k == 0): sum += key * dict1[key]
        return sum
                
