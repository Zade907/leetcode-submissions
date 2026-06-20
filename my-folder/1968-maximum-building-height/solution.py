class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])

        restrictions.sort()

        m = len(restrictions)

        # Left -> Right
        for i in range(1, m):
            idx1, h1 = restrictions[i - 1]
            idx2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, 
            h1 + (idx2 - idx1))

        for i in range(m - 2 , -1, -1):
            idx1, h1 = restrictions[i]
            idx2, h2 = restrictions[i + 1]
            restrictions[i][1] = min(h1,
            h2 + (idx2 - idx1))  
        ans = 0
        for i in range(1, m):
            idx1, h1 = restrictions[i - 1]
            idx2, h2 = restrictions[i]

            d = idx2 - idx1

            ans = max(
                ans,
                (h1 + h2 + d) // 2
            )

        return ans
