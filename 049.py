class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for s in strs:
            temp = list(s)
            temp.sort()
            key = ''.join(temp)
            try:
                ans[key].append(s)
                ans[key].sort()
            except KeyError:
                ans[key] = [s]
        return ans.values()