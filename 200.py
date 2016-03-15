class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        def explore(x,y):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[x]) or grid[x][y]=='0':
                return
            grid[x][y] = '0'
            explore(x-1,y)
            explore(x+1,y)
            explore(x,y-1)
            explore(x,y+1)
        ans = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] == '1':
                    explore(i,j)
                    ans = ans + 1
        return ans
        