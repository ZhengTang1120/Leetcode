class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1]
        index2 = 0
        index3 = 0
        index5 = 0
        for i in range(1,n):
            val = min(nums[index2]*2,nums[index3]*3,nums[index5]*5)
            if val == nums[index2]*2:
                index2 += 1
            if val == nums[index3]*3:
                index3 += 1
            if val == nums[index5]*5:
                index5 += 1
            nums.append(val)
        return nums[-1]