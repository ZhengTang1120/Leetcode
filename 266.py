class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counts = {}
        for c in s:
            try:
                counts[c]+=1
            except KeyError:
                counts[c] = 1
        i = 0
        for c in counts:
            if counts[c]%2 != 0:
                i+=1
                if i > 1:
                    return False
        return True