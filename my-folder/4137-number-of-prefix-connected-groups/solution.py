class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        prefixDict = {}
        count = 0
        for word in words:
            if len(word) < k:
                continue
            pref = word[:k]
            if pref in prefixDict:
                prefixDict[pref] += 1
                if prefixDict[pref] == 2:
                    count += 1 
            else:
                prefixDict[pref] = 1
        return count
