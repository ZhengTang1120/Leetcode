# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        lt = ListNode(0)
        l = lt
        de = 0
        while l1!=None and l2!=None:
            s = de+l1.val+l2.val
            if s>=10:
                lt.next = ListNode(s%10)
                de = 1
            else:
                lt.next = ListNode(s)
                de = 0
            l1 = l1.next
            l2 = l2.next
            lt = lt.next
        if l1:
            if de == 1:
               while l1:
                  s = de+l1.val 
                  if s>=10:
                      lt.next = ListNode(s%10)
                      de = 1
                  else:
                      de = 0
                      lt.next = ListNode(s)
                  l1 = l1.next
                  lt = lt.next
               if de == 1:
                   lt.next = ListNode(1)
                   return l.next
               else:
                   return l.next
            else:
                lt.next = l1
                return l.next
        elif l2:
            if de == 1:
               while l2:
                  s = de+l2.val 
                  if s>=10:
                      lt.next = ListNode(s%10)
                      de = 1
                  else:
                      de = 0
                      lt.next = ListNode(s)
                  l2 = l2.next
                  lt = lt.next
               if de == 1:
                   lt.next = ListNode(1)
                   return l.next
               else:
                   return l.next
            else:
                lt.next = l2
                return l.next
        else:
            if de == 1:
                lt.next = ListNode(1)
                return l.next
            else:
                return l.next