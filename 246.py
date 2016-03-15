class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num_dict = {"6":"9","8":"8","1":"1","0":"0","9":"6"}
        
        mid = int(math.ceil(len(num)/2.0))
        for i in xrange(mid):
            try:
                if num[-i-1] != num_dict[num[i]]:
                    return False
            except KeyError:
                return False
        return True