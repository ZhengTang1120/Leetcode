# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        elif head.next == None:
            return head
        else:
            h = head
            l = head.next
            h.next = None
            while(l):
                n = l.next
                l.next = h
                h = l
                l = n
            return h
            