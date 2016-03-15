class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        temp = num
        while True:
            if num%5==0:
                temp = num/5
            if num%3==0:
                temp = num/3
            if num%2==0:
                temp=num/2
            if temp == 1:
                return True
            elif temp == num:
                return False
            num = temp
            