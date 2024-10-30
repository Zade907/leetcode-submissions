class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = []
        double = []
        sum1 = 0
        sum2 = 0
        for i in range (len(nums)):
            if nums[i]<10:
                single.append(nums[i])
            else:
                double.append(nums[i])
        for i in range (len(single)):
            sum1 += single[i]
        for i in range (len(double)):
            sum2 += double[i]
        return sum1 != sum2
