class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        target = tuple(target)
        seen = set(tuple(p) for p in points)
        if target in seen:
            return 0
        if len(points) == 1:
            return -1
        gen = 0

        while True:
            gen += 1
            new = set()

            pts = list(seen)
            for i in range(len(pts)):
                for j in range(i + 1, len(pts)):
                    a, b = pts[i], pts[j]
                    mid = (
                        (a[0] + b[0]) // 2,
                        (a[1] + b[1]) // 2,
                        (a[2] + b[2]) // 2
                    )
                    if mid not in seen:
                        new.add(mid)

            if not new:
                return -1

            if target in new:
                return gen

            seen.update(new)

            if len(seen) >= 343:
                return -1
