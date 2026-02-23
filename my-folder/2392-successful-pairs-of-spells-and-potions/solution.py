class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(spells)
        m = len(potions)
        viable = []
        for i in range(n):
            target = math.ceil(success / spells[i])
            left,right = 0, m - 1
            successfulCount = 0
            if target > potions[right]:
                viable.append(successfulCount)
                continue
            while left <= right :
                mid = (left + right)//2
                if potions[mid] < target:
                    left = mid + 1
                elif potions[mid] >= target:
                    right = mid - 1
                    successfulCount = max(successfulCount, m - mid)
            viable.append(successfulCount)
        return viable



