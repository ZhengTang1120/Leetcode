class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        ans = nums[0]+nums[1]+nums[2]
        nums.sort()
        for i in range(0,len(nums)):
            if (i == 0 or nums[i-1]!=nums[i]):
                l = i+1
                r = len(nums)-1
                while l<r:
                    if nums[l]+nums[r]+nums[i]==target:
                        return target
                    elif nums[l]+nums[r]+nums[i]<target:
                        if abs(ans-target)>abs(nums[l]+nums[r]+nums[i]-target):
                            ans = nums[l]+nums[r]+nums[i]
                        l+=1
                    else:
                        if abs(ans-target)>abs(nums[l]+nums[r]+nums[i]-target):
                            ans = nums[l]+nums[r]+nums[i]
                        r-=1
        return ans