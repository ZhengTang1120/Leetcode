class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        pairsdict = {}
        ans = []
        if len(nums)<4:
            return ans
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                temp = [i,j]
                if nums[i]+nums[j] not in pairsdict:
                    pairsdict[nums[i]+nums[j]]=[temp]
                else:
                    if temp not in pairsdict[nums[i]+nums[j]]:
                        pairsdict[nums[i]+nums[j]].append(temp)
        values = sorted(pairsdict)
        numdic = {}
        for i in range(0,len(values)):
            if len(pairsdict[values[i]])>1 and 2*values[i]==target:
                for l in pairsdict[values[i]]:
                    for ll in pairsdict[values[i]]:
                        if l[0] not in ll and l[1] not in ll:
                            temp = [nums[l[0]],nums[l[1]],nums[ll[0]],nums[ll[1]]]
                            temp.sort()
                            if temp not in ans:
                                ans.append(temp)
            if target-values[i] in numdic:
                for l in pairsdict[values[i]]:
                    for ll in pairsdict[target-values[i]]:
                        if l[0] not in ll and l[1] not in ll:
                            temp = [nums[l[0]],nums[l[1]],nums[ll[0]],nums[ll[1]]]
                            temp.sort()
                            if temp not in ans:
                                ans.append(temp)
            numdic[values[i]] = i + 1
        return ans
