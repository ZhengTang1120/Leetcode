class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs)==0:
            return 0
        for i in xrange(1,len(costs)):
            for j in xrange(3):
                costs[i][j] += min(costs[i-1][(j+1)%3],costs[i-1][(j+2)%3])
        return min(costs[-1])