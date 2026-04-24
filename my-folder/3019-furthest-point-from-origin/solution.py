class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        from collections import Counter
        freq = Counter(moves)
        return abs(freq['L'] - freq['R']) + freq["_"]
        
