class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        s = 0
        e = len(matrix)-1
        #if n > 3:
            #self.rotate(matrix[1:n-1][1:n-1])
        while s<e:
            for i in xrange(s,e):
                temp = matrix[i][e]
                matrix[i][e] = matrix[s][i]
                matrix[s][i] = temp
                temp = matrix[e][e-i+s]
                matrix[e][e-i+s] = matrix[s][i]
                matrix[s][i] = temp
                temp = matrix[e-i+s][s]
                matrix[e-i+s][s] = matrix[s][i]
                matrix[s][i] = temp
            e-=1
            s+=1
            