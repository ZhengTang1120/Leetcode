class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        l = len(prices)
        if l == 0 or l == 1:
            return 0
        for i in xrange(1,l):
            if prices[i] > prices[i-1]:
                max += prices[i] - prices[i-1]
        return max