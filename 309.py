class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        buy = -prices[0]
        sell = 0
        buy_1 = -prices[0]
        sell_1 = 0
        sell_2 = 0
        for price in prices:
            buy = max(sell_2-price,buy_1)
            sell = max(buy_1+price,sell_1)
            buy_1 = buy
            sell_2 = sell_1
            sell_1 = sell
        return sell