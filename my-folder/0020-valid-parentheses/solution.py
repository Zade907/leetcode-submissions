class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBracket = {"(":")","{":"}","[":"]"}
        for i in s:
            if i in openBracket:
                stack.append(i)
            else:
                if not stack:
                    return False

                top = stack.pop()
                if i == openBracket[top]:
                    continue
                else:
                    return False
        return len(stack) == 0
