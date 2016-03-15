class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ans = len(words)
        pre = ""
        pos = -1
        for i,w in enumerate(words):
            if pos == -1 and (w == word1 or w == word2):
                pre = w
                pos = i
            elif (w == word1 or w == word2) and pre != w:
                ans = min(ans,i-pos)
                pos = i
                pre = w
            if pre == w:
                pos = i
        return ans