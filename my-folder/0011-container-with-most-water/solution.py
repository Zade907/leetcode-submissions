class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        n = len(height)
        j = n -1
        product = 0
        while(i<n-1 and j > 0) :
            if(product < (j-i)*min(height[j],height[i]) or product == 0):
                product = (j-i)*min(height[j],height[i])
            if height[i] < height[j]:
                i += 1 
            else:
                j -= 1 
        return product

