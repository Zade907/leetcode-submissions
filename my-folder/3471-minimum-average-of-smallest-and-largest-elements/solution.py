class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        while(len(nums)>0):
            avg = (max(nums)+min(nums))/2
            nums.remove(max(nums))
            nums.remove(min(nums))
            averages.append(avg)
        return min(averages)

            



