class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if s == '' or numRows == 1:
            return s
        result = ''
        for i in range(0,len(s),2*numRows-2):
            result = result + s[i]
        for j in range(1,numRows-1):
            for i in range(j,len(s),2*numRows-2):
                result = result + s[i]
                if i+2*numRows-2-2*j < len(s):
                    result = result + s[i+2*numRows-2-2*j]
        for i in range(numRows-1,len(s),2*numRows-2):
            result = result + s[i]
        return result