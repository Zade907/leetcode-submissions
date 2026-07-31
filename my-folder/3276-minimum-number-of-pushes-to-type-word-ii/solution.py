class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sortedFreq = freq.most_common()
        print(sortedFreq)
        
        minCost = 0
        currMultiplier = 1
        alloted = 0
        for i,j in sortedFreq:
            minCost += currMultiplier * j
            alloted += 1
            currMultiplier = (alloted // 8) + 1
        return minCost

            
