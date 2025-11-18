class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import Counter
        row_map = Counter(tuple(row) for row in grid)
        res = 0
        for col in zip(*grid):
            res += row_map[col]
        return res
