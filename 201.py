class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        offset = 0
        while m!=n:
            m>>=1
            n>>=1
            offset+=1
        return m<<offset