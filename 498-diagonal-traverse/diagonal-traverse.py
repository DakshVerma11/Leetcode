class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []

        for i in range(m + n - 1):
            if i % 2 == 0:
                x = min(i, m - 1)
                y = i - x
                while x >= 0 and y < n:
                    res.append(mat[x][y])
                    x -= 1
                    y += 1
            else:
                y = min(i, n - 1)
                x = i - y
                while y >= 0 and x < m:
                    res.append(mat[x][y])
                    x += 1
                    y -= 1

        return res