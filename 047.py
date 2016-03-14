class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        ans = []
        pre = "a"
        nums.sort()
        for i in xrange(len(nums)):
            if nums[i] != pre:
                temp = nums[:]
                del temp[i]
                for res in self.permuteUnique(temp):
                    res.insert(0,nums[i])
                    if res not in ans:
                        ans.append(res)
                pre = nums[i]
        return ans