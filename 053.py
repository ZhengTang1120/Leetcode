class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0]
        ans = nums[0]
        for i in xrange(1,len(nums)):
            temp = max(temp+nums[i],nums[i])
            ans = max(ans,temp)
        return ans