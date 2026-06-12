class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            currArea = (right - left) * min(height[left],height[right])
            maxArea = max(currArea, maxArea)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea

