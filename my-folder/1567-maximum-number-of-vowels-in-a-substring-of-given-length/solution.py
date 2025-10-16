class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        currentVowel = len([i for i in s[0:k] if i in vowels])
        maxVowel = currentVowel
        for i in range(k, len(s)):
            if s[i] in vowels : currentVowel += 1
            if s[i-k] in vowels : currentVowel -= 1
            maxVowel = max(maxVowel,currentVowel)
        return maxVowel
        


