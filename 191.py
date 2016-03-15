class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        binary = bin(n)[2:]
        sum = 0
        for i in binary:
            sum = sum + int(i)
        return sum