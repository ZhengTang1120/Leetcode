class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin1 = bin(n)[2:]
        bin2 = ''
        for i in range(len(bin1)-1,-1,-1):
            bin2 = bin2 + bin1[i]
        for i in range(31,len(bin1)-1,-1):
            bin2 = bin2 + '0'
        n2 = int(bin2,2)
        return n2