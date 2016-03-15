class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        opt = [nums[0]]
        if nums[1]>nums[0]:
            opt.append(nums[1])
        else:
            opt.append(nums[0])
        for i in xrange(2,len(nums)):
            opt.append(max(opt[i-1],opt[i-2]+nums[i]))
        return opt[len(nums)-1]