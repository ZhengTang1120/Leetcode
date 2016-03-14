class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        maxnum = nums[0]
        d = {}
        t = {}
        d[0] = nums[0]
        t[0] = nums[0]
        for i in range(1,len(nums)):
            d[i] = max(nums[i],nums[i]*d[i-1],nums[i]*t[i-1])
            t[i] = min(nums[i],nums[i]*d[i-1],nums[i]*t[i-1])
            maxnum = max(maxnum,d[i])
        return maxnum