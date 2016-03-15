class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return True if math.log10(n)/math.log10(3) - int(math.log10(n)/math.log10(3)) == 0 else False