class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s)==len(goal)):
            s1 = s + s 
            return goal in s1
        else:
            return False
