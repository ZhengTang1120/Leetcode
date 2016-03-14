/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *reverse(ListNode *head,int n) {
        ListNode *cur = head->next;
        ListNode *tail = head->next;
        ListNode *next = cur->next;
        for(int i=0;i<n;i++){
            head->next = next;
            tail->next = next->next;
            next->next = cur;
            next = tail->next;
            cur = head->next;
        }
        return head;
    }
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        if(m == n)
            return head;
        ListNode *h = new ListNode(0);
        h->next = head;
        ListNode *result = h;
        for(int i=0;i<m-1;i++)
            h = h->next;
        h = reverse(h,n-m);
        return result->next;
    }
};