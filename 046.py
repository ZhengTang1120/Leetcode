class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        ans = []
        for num in nums:
            temp = nums[:]
            temp.remove(num)
            for res in self.permute(temp):
                res.insert(0,num)
                ans.append(res)
        return ans