class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        list1 = []
        for i in range (len(height)-1):
            if height[i]>threshold:
                list1.append(i+1)
        return list1
