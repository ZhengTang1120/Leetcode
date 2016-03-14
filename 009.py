class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        while len(s) > 1:
            if int(s[0])!=int(s)%10:
                return False
            s = s[1:]
            s = s[:-1]
        return True
            