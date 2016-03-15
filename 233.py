class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        ans = 0
        for i in range(0,n+1):
            s = str(i)
            for c in s:
                if c == '1':
                    ans = ans + 1
                    break
        return ans
            