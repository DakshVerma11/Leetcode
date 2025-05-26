class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum=0
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                sum+=self.matrix[i][j]
        return sum





class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        
        m, n = len(matrix), len(matrix[0])
        self.sumrowmatrix = [[0] * (n + 1) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                self.sumrowmatrix[i][j + 1] = self.sumrowmatrix[i][j] + matrix[i][j]




    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        total = 0
        for i in range(row1, row2 + 1):
            total += self.sumrowmatrix[i][col2 + 1] - self.sumrowmatrix[i][col1]
        return total












class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        
        m, n = len(matrix), len(matrix[0])
        # Extra row and column for easier prefix calculation
        self.summatrix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                self.summatrix[i + 1][j + 1] = (matrix[i][j] + self.summatrix[i + 1][j] + self.summatrix[i][j + 1] - self.summatrix[i][j])




    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.summatrix[row2+1][col2+1]-self.summatrix[row1][col2+1]-self.summatrix[row2+1][col1]+self.summatrix[row1][col1]
