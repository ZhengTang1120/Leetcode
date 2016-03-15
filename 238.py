class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        n = 1
        p = nums[0]
        f = -1
        c = 0
        for i in range(1,len(nums)):
            if nums[i] == 0:
                f = i
                c = c + 1
            else:
                p = p * nums[i]
        if f!=-1:
            if c > 1:
                return [0]*len(nums)
            nums = [0]*len(nums)
            nums[f] = p
            return nums
        for i in range(0,len(nums)):
            nums[i] = p/nums[i]
        return nums