class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freq = {}
        minDist = float("inf")
        for i,j in enumerate(nums):
            if j not in freq:
                freq[j] = [i]
            else:
                freq[j].append(i)
                if len(freq[j]) == 3:
                    a,b,c = freq[j]
                    minDist = min(minDist, 2 * (c - a))
                    freq[j].pop(0)
        return -1 if minDist == float("inf") else minDist
