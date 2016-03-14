class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        ans = []
        
        while left<right and top<bottom:
            li1 = matrix[top][left:right]
            li2 = [x[right-1] for x in matrix[top+1:bottom-1]]
            if bottom - 1 != top:
                li3 = matrix[bottom-1][left:right]
                li3.reverse()
            else:
                li3 = []
            if left != right-1:
                li4 = [x[left] for x in matrix[top+1:bottom-1]]
                li4.reverse()
            else:
                li4 = []
            ans += li1+li2+li3+li4
            top+=1
            left+=1
            bottom-=1
            right-=1
        return ans
            