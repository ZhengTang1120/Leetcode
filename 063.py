class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0 for col in range(n)] for row in range(m)]  
        for i in range(0,m):
            if obstacleGrid[i][0] == 0:
                res[i][0] = 1
            else:
                break
        for j in range(0,n):
            if obstacleGrid[0][j] == 0:
                res[0][j] = 1
            else:
                break            
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    res[i][j] = res[i][j-1] + res[i-1][j]
                else:
                    res[i][j] = 0
        return res[m-1][n-1]
        