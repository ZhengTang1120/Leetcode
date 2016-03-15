class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) == 1:
            if k > 0:
                return False
        if len(nums) <= k:
            nums.sort()
            for j in range(0,len(nums)-1):
                if nums[j] == nums[j+1]:
                    return True
        for i in range(0,len(nums)-k):
            temp = nums[i:i+k+1]
            temp.sort()
            for j in range(0,k):
                if temp[j] == temp[j+1]:
                    return True
        return False