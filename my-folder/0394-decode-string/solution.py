class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                currStr = ""
                k = ""
                while stack[-1] != "[":
                    currStr = stack.pop() + currStr
                stack.pop()
                
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)
                stack.append(currStr*k)
        return "".join(stack)



