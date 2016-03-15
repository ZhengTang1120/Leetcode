class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        nums = sorted(nums,reverse=True)
        return nums[k-1]