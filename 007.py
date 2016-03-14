class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        s = str(x)
        t = 0
        if x == 0:
            return x
        elif x > 0: 
            for i in range(0,len(s)):
                t = t + int(s[i])*pow(10,i)
        else:
            s = s[1:]
            for i in range(0,len(s)):
                t = t + int(s[i])*pow(10,i)
            t = t * -1
        if t > 2147483648 or t < -2147483648:
            t = 0
        return t