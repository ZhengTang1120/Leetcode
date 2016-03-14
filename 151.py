class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if s.strip()=='':
            return ''
        s = s.split(' ')
        ans = s.pop()
        while len(s)!=0:
            t = s.pop()
            if t.strip()!='':
                if ans == '':
                    ans = t
                else:
                    ans = ans+' '+t
        return ans