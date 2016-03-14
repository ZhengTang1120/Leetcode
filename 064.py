class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
             return 0
        opt =  [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        opt[0][0] = grid[0][0]
        for i in xrange(1,len(grid)):
            opt[i][0] = grid[i][0]+opt[i-1][0]
        for i in xrange(1,len(grid[0])):
            opt[0][i] = grid[0][i]+opt[0][i-1]
        for i in xrange(1,len(grid)):
            for j in xrange(1,len(grid[0])):
                opt[i][j] = min((opt[i-1][j]+grid[i][j]),(opt[i][j-1]+grid[i][j]))
        return opt[len(grid)-1][len(grid[0])-1]