# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = []
        ans = {}
        queue.append((root,0))
        while(len(queue)!=0):
            temp = queue[0]
            try:
                ans[temp[1]].append(temp[0].val)
            except KeyError:
                ans[temp[1]] = [temp[0].val]
            del queue[0]
            if temp[0].left != None:
                queue.append((temp[0].left,temp[1]+1))
            if temp[0].right != None:
                queue.append((temp[0].right,temp[1]+1))
        for i in ans:
            if i%2 != 0:
                ans[i].reverse()
        return ans.values()
            