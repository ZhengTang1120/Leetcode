class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return k
        pre1 = k
        pre2 = k*k
        ans = k*k
        for i in xrange(2,n):
            ans = (k-1)*pre1+(k-1)*pre2
            pre1 = pre2
            pre2 = ans
        return ans
        