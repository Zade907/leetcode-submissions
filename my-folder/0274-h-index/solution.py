class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i in range(len(citations)):
            if citations[i] < n:
                n -= 1 
            elif citations[i] > n:
                return n
        return n 

