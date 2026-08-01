from collections import Counter, defaultdict

class Solution:
    def maximumWidth(self, planks: List[int]) -> int:
        planks.sort()
        freq = Counter(planks)
        freq2 = defaultdict(int)

        nums = list(freq.keys())
        m = len(nums)

        for i in range(m):
            x = nums[i]
            freq2[x] += freq[x]

            freq2[2 * x] += freq[x] // 2

            for j in range(i + 1, m):
                y = nums[j]
                freq2[x + y] += min(freq[x], freq[y])

        return max(freq2.values())
