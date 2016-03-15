class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s1 = []
        for i in range(0,len(s)):
            if s[i]!=' ':
                if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
                    s1.append(s[i])
                else:
                    t = 0
                    while i < len(s) and s[i]!=' ' and s[i]!='+'and s[i]!='-'and s[i]!='*'and s[i]!='/':
                        t = t*10+int(s[i])
                        i = i + 1
                    s1.append(t)
        s = []
        for i in range(0,len(s1)):
            if s1[i] == '*':
                s.append(s.pop()*s1[i+1])
                i = i + 1
            elif s1[i] == '/':
                s.append(s.pop()*s1[i+1])
                i = i + 1
            else:
                s.append(s1[i])
        s1 = []
        for i in range(0,len(s)):
            if s[i] == '+':
                s1.append(s1.pop()+s[i+1])
                i = i + 1
            elif s[i] == '-':
                s1.append(s1.pop()*s[i+1])
                i = i + 1
            else:
                s1.append(s[i]) 
        return s1[0]
