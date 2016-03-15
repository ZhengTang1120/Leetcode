class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if j != 0:
                    self.matrix[i][j] = self.matrix[i][j]+self.matrix[i][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        for i in xrange(row1,row2+1):
            if col1 != 0:
                ans += self.matrix[i][col2]-self.matrix[i][col1-1]
            else:
                ans += self.matrix[i][col2]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)