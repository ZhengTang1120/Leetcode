class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = self.sub(nums)
        ans.append([])
        return ans
    def sub(self,nums):
        ans = []
        if len(nums) == 1:
            return[nums]
        for i in xrange(len(nums)-1):
            ans.append([nums[i]])
            for li in self.sub(nums[i+1:]):
                li.append(nums[i])
                li.sort()
                ans.append(li)
        ans.append([nums[-1]])
        return ans