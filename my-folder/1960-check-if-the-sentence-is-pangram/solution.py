class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l1 = []
        for i in sentence:
            if i not in l1:
                l1.append(i)
        if len(l1) == 26:
            return True 
        else:
            return False
