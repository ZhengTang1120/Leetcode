class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        height.append(0)
        stack = []
        i = 0
        maxRec = 0
        while (i<len(height)):
            if len(stack)==0 or height[stack[-1]] <= height[i]:
                stack.append(i)
                i = i + 1
            else:
                t = stack.pop()
                if len(stack) == 0:
                    maxRec = max(maxRec,height[t]*i)
                else:
                    maxRec = max(maxRec,height[t]*(i-stack[-1]-1))
        return maxRec