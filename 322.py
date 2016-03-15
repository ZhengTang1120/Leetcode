class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans = [-1 for i in range(amount+1)]
        if amount==0:
            return 0
        ans[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if (i-c>=0 and ans[i-c]!=-1) and (ans[i-c]+1<ans[i] or ans[i] == -1):
                    ans[i] = ans[i-c]+1
        return ans[amount]