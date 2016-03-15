# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        def lheight(root):
            l = 0
            while root!=None:
                l = l + 1
                root = root.left
            return l
        def rheight(root):
            r = 0
            while root!=None:
                r = r + 1
                root = root.right
            return r
        def count(root):
            if lheight(root) == rheight(root):
                return pow(2,lheight(root)) - 1
            else:
                return count(root.left) + count(root.right)  + 1
        return count(root)
            