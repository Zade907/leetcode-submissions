class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited = set()
        freq = Counter(s)
        stack = []

        for c in s:
            freq[c] -= 1 

            if c in visited:
                continue
            
            while stack and stack[-1] > c and freq[stack[-1]]:
                visited.remove(stack.pop())

            stack.append(c)
            visited.add(c)
        return "".join(stack)

