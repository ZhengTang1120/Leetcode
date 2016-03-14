class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[1 for col in range(n)] for row in range(m)]  
        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = res[i][j-1] + res[i-1][j]
        return res[m-1][n-1]