# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        def traverse(root):
            if root != None:
                root.left,root.right = root.right,root.left
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return root
        