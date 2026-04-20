class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxDist = float(-inf)
        for i in range(len(colors)-1):
            for j in range(i + 1, len(colors)):
                if colors[i] != colors[j]:
                    maxDist = max((j - i),  maxDist)
        return maxDist
