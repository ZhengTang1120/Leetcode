class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return True
        i = 0
        maxstep = nums[0]
        for i in xrange(1,len(nums)):
            if maxstep == 0:
                return  False
            maxstep -= 1
            if maxstep<nums[i]:
                maxstep = nums[i]
            if maxstep+i>=len(nums)-1:
                return True
                
                