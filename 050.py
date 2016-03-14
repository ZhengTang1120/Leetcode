class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        def powalg(x,n):
            if n == 0:
                return 1.0
            half = powalg(x,n//2)
            if n%2 == 0:
                return half*half
            else:
                return half*half*x
        if n > 0:
            return powalg(x,n)
        else:
            return 1/powalg(x,-n)