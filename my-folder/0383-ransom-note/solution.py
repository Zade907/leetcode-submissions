class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        ransomCount = Counter(ransomNote)
        magCount = Counter(magazine)
        for key,value in ransomCount.items():
            if key not in magCount or magCount[key] < value:
                return False
        return True
