class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if s[0] == "0":
            return 0
        else:
            ans = [1,1]
        for i in xrange(2,len(s)+1):
            if int(s[i-1])>0:
                if int(s[i-2:i]) >0:
                    if int(s[i-2:i]) <= 26 and s[i-2] != "0":
                        ans.append(ans[i-1]+ans[i-2])
                    else:
                        ans.append(ans[i-1])
                else:
                    ans.append(ans[i-2])
            else:
                if 0< int(s[i-2]) <=2:
                    ans.append(ans[i-2])
                else:
                    ans.append(0)
        return ans[len(s)]