class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum = -999
        temp = 0
        for i in range(0,len(gain)):
            if(temp>maximum):
                maximum = temp
            temp += gain[i]
        return max(maximum,temp)
