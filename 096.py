class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = [1,1]
         
        for i in xrange(2,n+1):
            temp = 0
            for j in xrange(i):
                temp += num[j]*num[i-1-j]
            num.append(temp)
        return num[n]