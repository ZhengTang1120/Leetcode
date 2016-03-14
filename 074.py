class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        left = 0
        right = len(matrix)-1
        while left<=right:
            loc = left + (right-left)/2
            if target == matrix[loc][0]:
                return True
            if target > matrix[loc][0]:
                left = loc+1
            else:
                right = loc-1
        loc = right
        left = 0
        right = len(matrix[loc])-1
        while left<=right:
            loc2 = left + (right-left)/2
            if target == matrix[loc][loc2]:
                return True
            if target > matrix[loc][loc2]:
                left = loc2+1
            else:
                right = loc2-1
        return False
        