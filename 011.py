class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        i = 0
        j = len(height)-1
        while(i<j):
            ans = max(ans,(j-i)*min(height[i],height[j]))
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return ans
            