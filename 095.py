# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateTree(s,e):
            result = []
            if s>e:
                result.append(None)
                return result
            for i in xrange(s,e+1):
                l = generateTree(s,i-1)
                r = generateTree(i+1,e)
                for j in xrange(len(l)):
                    for k in xrange(len(r)):
                        temp = TreeNode(i)
                        temp.left = l[j]
                        temp.right = r[k]
                        result.append(temp)
            return result
        if n == 0:
            return []
        return generateTree(1,n)
                    