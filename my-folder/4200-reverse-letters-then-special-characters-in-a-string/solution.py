class Solution:
    def reverseByType(self, s: str) -> str:
        result = ""
        char, specialChar = len(s) - 1,len(s) - 1
        i = 0
        while i < len(s):
            if s[i].isalpha():
                while char >= 0 and not s[char].isalpha() :
                    char -= 1
                result += s[char]
                char -= 1
            else:
                while specialChar >= 0 and s[specialChar].isalpha() :
                    specialChar -= 1
                result += s[specialChar]
                specialChar -= 1
            i += 1
        return result
                
                    
            
