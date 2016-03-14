# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder = inorder
        self.postorder = postorder
        root = self.build(0,len(postorder)-1,0,len(inorder)-1)
        return root
    def build(self,pstart,pend,istart,iend):
        if pstart>pend:
            return None
        root = TreeNode(self.postorder[pend])
        if pstart == pend:
            return root
        loc = self.inorder.index(root.val)
        root.left = self.build(pstart,pstart+loc-istart-1,istart,loc-1)
        root.right = self.build(pend-iend+loc,pend-1,loc+1,iend)
        return root