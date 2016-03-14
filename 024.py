# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        ans.next = head
        temp = ans
        while temp.next != None:
            node1 = temp.next
            node2 = node1.next
            if node2 == None:
                break
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = temp.next.next
            
        return ans.next