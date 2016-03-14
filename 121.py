class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        low = prices[0]
        profit = 0
        for price in prices:
            if price<low:
                low = price
            if price - low > profit:
                profit = price - low
        return profit
        