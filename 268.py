class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        pre = nums[0]
        for num in nums[1:]:
            if num-pre==2:
                return num-1
            else:
                pre = num
        if pre == nums[-1]:
            if nums[0]==0:
                return pre+1
            else:
                return 0