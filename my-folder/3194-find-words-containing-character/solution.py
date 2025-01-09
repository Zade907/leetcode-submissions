class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l1 = []
        for i in range (len(words)):
            if x in words[i]:
                 l1.append(i)
        return l1
