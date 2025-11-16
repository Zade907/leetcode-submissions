class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        freq = Counter(arr)
        return len(freq) == len(set(freq.values()))
