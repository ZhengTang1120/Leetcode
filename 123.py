class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l < 2:
            return 0
        minp = prices[0]
        maxp = prices[l-1]
        prep = {0:0}
        posp = {l-1:0}
        for i in xrange(1,l):
            minp = min(minp,prices[i])
            maxp = max(maxp,prices[l-1-i])
            prep[i] = max(prep[i-1],prices[i]-minp)
            posp[l-i-1] = max(posp[l-i],maxp-prices[l-i-1])
        ans = 0
        for i in xrange(0,l):
            ans = max(ans,prep[i]+posp[i])
        return ans
            
        