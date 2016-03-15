# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        temp = []
        ans = []
        def leveltraverse(root,level):
            if root==None or level<0:
                return 0
            if level == 0:
                temp.append(root.val)
                return 1
            return leveltraverse(root.left,level-1)+leveltraverse(root.right,level-1)
        i = 0
        while (1):
            if not leveltraverse(root,i):
                break
            else:
                ans.append(temp[-1])
            i = i + 1
        return ans
            