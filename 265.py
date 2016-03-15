class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs)==0 or len(costs[0])==0:
            return 0
        for i in xrange(1,len(costs)):
            min1 = {0:sys.maxint}
            min2 = {len(costs[i])-1:sys.maxint}
            for j in xrange(1,len(costs[i])):
                min1[j] = min(min1[j-1],costs[i-1][j-1])
                min2[len(costs[i])-j-1] = min(min2[len(costs[i])-j],costs[i-1][len(costs[i])-j])
            for j in xrange(len(costs[i])):
                costs[i][j] += min(min1[j],min2[j])
        costs[-1].append(sys.maxint)
        return min(costs[-1])