# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        def traverse(root,num):
            if root == None:
                return 0
            num = num * 10 + root.val
            if root.left == None and root.right == None:
                return num
            else:
                return traverse(root.left,num) + traverse(root.right,num)
        
        return traverse(root,0)