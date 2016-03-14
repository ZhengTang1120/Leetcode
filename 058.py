class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if(s == '')
            return 0;
        i = len(s.split(''));
        ls = s.split()[i-1];
        return ls.size();