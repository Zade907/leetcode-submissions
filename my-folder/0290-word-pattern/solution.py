class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        order = {}
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        visited = []
        for i in range(len(pattern)):
            if pattern[i] not in order and words[i] not in visited:
                order[pattern[i]] = words[i]
                visited.append(words[i])
            else:
                if pattern[i] not in order or order[pattern[i]] != words[i]:
                    return False
        return True
                
