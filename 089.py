class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        ans = []
        ans += self.grayCode(n-1)
        nums = self.grayCode(n-1)
        nums.reverse()
        for num in nums:
            ans.append(2**(n-1)+num)
        return ans