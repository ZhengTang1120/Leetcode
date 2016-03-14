# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    pre = None
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if not(self.isValidBST(root.left)):
            return False
        if self.pre!=None and self.pre>=root.val:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
        