class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        for i in xrange(1,n):
            temp = triangle[i][0]
            triangle[i][0] = triangle[i-1][0] + temp
            temp = triangle[i][i]
            triangle[i][i] = triangle[i-1][i-1] + temp
            for j in xrange(1,i):
                temp = triangle[i][j]
                triangle[i][j] = min(triangle[i-1][j],triangle[i-1][j-1])+temp
        return min(triangle[n-1])