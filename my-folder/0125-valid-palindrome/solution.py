class Solution:
    def isPalindrome(self, s: str) -> bool:
        character = [c.lower() for c in s if c.isalnum()]
        return character == character[::-1]
