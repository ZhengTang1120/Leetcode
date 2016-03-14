class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        numdic = {}
        for i in range(0,len(nums)):
            if target-nums[i] in numdic:
                return [numdic[target-nums[i]],i+1]
            numdic[nums[i]] = i + 1