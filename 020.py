class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        l = []
        for i in range(0,len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                l.append(s[i])
            elif len(l) == 0:
                return False
            else:
                temp = l.pop()
                if not((s[i] == ')' and temp == '(') or (s[i] == ']' and temp == '[') or (s[i] == '}' and temp == '{')):
                    return False
        if len(l) > 0:
            return False
        return True