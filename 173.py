# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.queue = self.traverse(root)
    
    def traverse(self,root):
        if root == None:
            return []
        queue = self.traverse(root.left)+[root.val]+self.traverse(root.right)
        return queue
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.queue) == 0:
            return False
        else:
            return True

    def next(self):
        """
        :rtype: int
        """
        temp = self.queue[0]
        del self.queue[0]
        return temp

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())