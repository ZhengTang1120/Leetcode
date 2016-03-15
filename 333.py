# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    pre = None
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.pre = None
        if self.isValidBST(root):
            return self.nodesum(root)
        return max(self.largestBSTSubtree(root.left),self.largestBSTSubtree(root.right))
    def nodesum(self,root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return self.nodesum(root.left)+self.nodesum(root.right)+1
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