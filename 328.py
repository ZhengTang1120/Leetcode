# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        odd = head
        even = odd.next
        ot = odd
        et = even
        while(ot.next!=None and et.next!=None):
            ot.next = et.next
            ot = ot.next
            et.next = ot.next
            et = et.next
        ot.next = even
        return odd
        