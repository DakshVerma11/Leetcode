class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        res = 0

        for i, (x1, y1) in enumerate(points):
            bottom = -float("inf")
            for x2, y2 in points[i+1:]:
                if bottom < y2 <= y1:
                    res += 1
                    bottom = y2
                    if y1 == bottom:
                        break

        return res
