class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        target = ""
        for word in words:
            charValue = 0
            for char in word:
                position = ord(char) - 97 
                charValue += weights[position]
            charValue = charValue % 26
            target += chr(122-charValue)
        return target
