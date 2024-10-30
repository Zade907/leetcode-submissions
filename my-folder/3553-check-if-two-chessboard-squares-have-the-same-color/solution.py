class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        first = ['a','c','e','g']
        if coordinate1[0] in first: column1 = 1
        else: column1 = 2
        if coordinate2[0] in first: column2 = 1
        else: column2 = 2
        black1 = (column1 + int(coordinate1[1]))%2
        black2 = (column2 + int(coordinate2[1]))%2
        return black1 == black2
        
