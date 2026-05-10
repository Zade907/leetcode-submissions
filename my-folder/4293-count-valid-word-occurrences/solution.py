class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = "".join(chunks)
        words = {}
        word = ""
        
        n = len(s)
        
        for i,ch in enumerate(s):
            if "a" <= ch <= "z":
                word += ch
            elif (ch == "-" and i > 0 and i < n -1 and "a" <= s[i - 1] <= "z" and "a" <= s[i + 1] <= "z"):
                word += ch
            else:
                if word:
                    words[word] = words.get(word, 0) + 1
                    word = ""
        if word:
            words[word] = words.get(word, 0) + 1
        return [words.get(q,0) for q in queries]
        
