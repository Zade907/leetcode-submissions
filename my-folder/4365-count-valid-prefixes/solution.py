class Solution:
    def countValidPrefixes(self, s: str) -> int:
        n = len(s)
        count = 0
        zeros = 0
        ones = 0
        for i in s:
            if i == "0":
                zeros += 1
            else:
                ones += 1
            if abs(zeros - ones) > 1:
                continue
            else:
                count += 1
        return count
