class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False
        for i in range(0,len(nums)-k):
            temp = sorted(nums[i:i+k])
            pre = temp[0]
            temp = temp[1:]
            for n in temp:
                if n-pre<=t:
                    return True
                pre = n
        return False