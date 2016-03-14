class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        numdict = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I" }
        ans = ''
        for i in sorted(numdict,reverse=True):
            while(num>=i):
                num-=i
                ans+=numdict[i]
        return ans