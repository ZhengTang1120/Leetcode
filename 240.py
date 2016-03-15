class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        i = 0
        j = len(matrix[0])-1
        while i<len(matrix) and j>=0:
            if target > matrix[i][j]:
                i = i + 1
            elif target < matrix[i][j]:
                j = j - 1
            else:
                return True
        return False