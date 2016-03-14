class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        start = ans = 0
        ex = {}
        for i in range(0,len(s)):
            if s[i] in ex:
                temp = ex[s[i]]+1
                for j in range(start,temp):
                    del ex[s[j]]
                start = temp
                ex[s[i]] = i
            else:
                ex[s[i]] = i
                if ans < i-start+1:
                    ans = i-start+1
        return ans