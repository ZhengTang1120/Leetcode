class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumnum = 0
        sumdict = {0:-1}
        result = 0
        for i in xrange(len(nums)):
            sumnum += nums[i]
            if sumnum not in sumdict:
                sumdict[sumnum] = i
            if sumnum - k in sumdict:
                result = max(result,i-sumdict[sumnum-k])
            
        return result