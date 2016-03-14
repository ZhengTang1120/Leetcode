class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        l = len(s)
        d = {}
        d[0] = True
        for i in range(1,len(s)+1):
            d[i] = False
            for j in range(0,i):
                if d[j] == True and s[j:i] in wordDict:
                    d[i] = True
                    break
        return d[len(s)]