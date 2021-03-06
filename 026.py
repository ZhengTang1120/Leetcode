class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for num in nums[1:]:
            if num != nums[i]:
                i+=1
                nums[i] = num
        return i+1