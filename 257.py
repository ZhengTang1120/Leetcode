# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        def getPath(root,s):
            if root != None:
                if root.left == None and root.right == None:
                    if s != '':
                        s = s + '->' + str(root.val)
                    else:
                        s = str(root.val)
                    ans.append(s)
                else:
                    if s != '':
                        s = s + '->' + str(root.val)
                    else:
                        s = str(root.val)
                    getPath(root.left,s)
                    getPath(root.right,s)
        if root == None:
            return ans
        else:
            getPath(root,'')
        return ans
                
            