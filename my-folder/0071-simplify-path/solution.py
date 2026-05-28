class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        res = []
        for dire in stack:
            if dire == "" or dire == ".":
                continue
            if dire == ".." :
                if res:
                    res.pop()
            else:
                res.append(dire)
        return "/" + "/".join(res)
