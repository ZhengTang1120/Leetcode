class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        temp = []
        while n != 1:
            strn='%d'%n
            n = 0
            for i in range(0,len(strn)):
              n = n + int(strn[i])*int(strn[i])
            if n in temp:
                return False
            if n not in temp:
                temp.append(n)
        return True