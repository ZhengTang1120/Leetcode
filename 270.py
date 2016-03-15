# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        ans = root.val
        diff = abs(root.val-target)
        while root!=None:
            if diff > abs(root.val-target):
                ans = root.val
                diff = abs(root.val-target)
            if root.val<target:
                root = root.right
            else:
                root = root.left
        return ans