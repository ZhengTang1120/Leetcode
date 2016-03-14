# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        temp1 = head
        temp2 = head
        for i in range(0,n):
            temp1 = temp1.next
            if not temp1:
                return head.next
        while temp1.next != None:
            temp2 = temp2.next
            temp1 = temp1.next
        temp2.next = temp2.next.next
        return head
            