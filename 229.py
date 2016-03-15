class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        a = None
        b = None
        ac = 0
        bc = 0
        for n in nums:
            if a == n:
                ac = ac + 1
            elif b == n:
                bc = bc + 1
            elif a == None:
                a = n
                ac = 1
            elif b == None:
                b = n
                bc = 1
            else:
                if ac < bc:
                    ac = ac - 1
                    if ac == 0:
                        a = n
                        ac = 1
                else:
                    bc = bc - 1
                    if bc == 0:
                        b = n
                        bc = 1
        ac = bc = 0
        result = []
        for n in nums:
            if a == n:
                ac = ac + 1
        if ac > len(nums)/3:
            result.append(a)
        for n in nums:
            if b == n:
                bc = bc + 1
        if bc > len(nums)/3:
            result.append(b) 
        return sorted(result)
                