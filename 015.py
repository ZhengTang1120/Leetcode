class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        ans = []
        if len(nums)<3:
            return ans
        nums.sort()
        for i in range(0,len(nums)):
            if (i == 0 or nums[i-1]!=nums[i]):
                l = i+1
                r = len(nums)-1
                while l<r:
                    if nums[l]+nums[r]==-nums[i]:
                        temp = [nums[l],nums[r],nums[i]]
                        temp.sort()
                        ans.append(temp)
                        while(l<r and nums[l]==nums[l+1]):
                            l+=1
                        while(l<r and nums[r]==nums[r-1]):
                            r-=1
                        l+=1
                        r-=1
                    elif nums[l]+nums[r]<-nums[i]:
                        l+=1
                    else:
                        r-=1
        return ans