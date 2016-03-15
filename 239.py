class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        ans = []
        deque = []
        for i in range(0,len(nums)):
            if len(deque)!=0 and deque[0] == i-k:
                deque = deque[1:]
            while len(deque)!=0 and nums[deque[-1]]<nums[i]:
                deque.pop()
            deque.append(i)
            if i >= k-1:
                ans.append(nums[deque[0]])
        return ans