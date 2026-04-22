class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for query in queries:
            for word in dictionary:
                count = 0
                for i in range(len(query)):
                    if query[i] != word[i]:
                        count+= 1
                if count <= 2:
                    res.append(query)
                    break
        return res
