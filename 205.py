class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        dict1 = {}
        dict2 = {}
        for i in range(0,len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = t[i]
            else:
                if dict1[s[i]] != t[i]:
                    return False
            if t[i] not in dict2:
                dict2[t[i]] = s[i]
            else:
                if dict2[t[i]] != s[i]:
                    return False
        return True