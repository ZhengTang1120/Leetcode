class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        l1 = list(s)
        l2 = list(t)
        l1.sort()
        l2.sort()
        if l1!=l2:
            return False
        else:
            return True
            