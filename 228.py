class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums)==0:
            return nums
        result = []
        pre = nums[0]
        s = [str(pre)]
        nums = nums[1:]
        for n in nums:
            if n-pre == 1:
                s.append(str(n))
            else:
                if len(s) == 1:
                    result.append(s[0])
                else:
                    t = s[0]+'->'+s[-1]
                    result.append(t)
                s = [str(n)]
            pre = n
        if len(s) == 1:
            result.append(s[0])
        else:
            t = s[0]+'->'+s[-1]
            result.append(t)
            s = [str(n)]
        return result