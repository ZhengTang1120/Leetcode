# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None
class Solution:
  # @param {TreeNode} root
  # @param {integer} k
  # @return {integer}
  def kthSmallest(self, root, k):
    stack = []
    node = root
    while node:
      stack.append(node)
      node = node.left
    x = 1
    while stack and x <= k:
      node = stack.pop()
      x += 1
      right = node.right
      while right:
        stack.append(right)
        right = right.left
    return node.val