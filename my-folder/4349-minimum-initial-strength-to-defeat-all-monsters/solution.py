class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        maxStrength = sum(monsters)
        n = len(monsters)

        diff = [0] * (n + 1)
        for l,r, bonus in boosts:
            diff[l] += bonus
            if r + 1 < n:
                diff[r + 1] -= bonus
        bonusStrength = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            bonusStrength[i] = curr
        print(bonusStrength)
        for i in range(n - 1, -1, -1):
            if bonusStrength[i] >= monsters[i]:
                maxStrength -= monsters[i]
            else:
                maxStrength -= bonusStrength[i]
                break
    
        return maxStrength
