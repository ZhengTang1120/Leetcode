class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        while n != 1:
            if n%2!=0:
                return False
            else:
                n = n // 2
        return True
        