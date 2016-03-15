class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if matrix == []:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for x in range(m)]
        length = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                length = max(length,dp[i][j])
        return length*length