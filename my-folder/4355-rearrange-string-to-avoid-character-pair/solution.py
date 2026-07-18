class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        freq = Counter(s)
        t = ""
        for i in range(freq[y]):
            t += y 
        for i in s:
            if i != y:
                t += i
        return t
