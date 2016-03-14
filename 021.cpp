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
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        if(l1 == NULL && l2 == NULL)
            return NULL;
        else if(l1 == NULL)
            return l2;
        else if(l2 == NULL)
            return l1;
        ListNode *ltemp = new ListNode(0);
        ListNode *head = ltemp;
        while(l1!=NULL && l2!=NULL){
            if(l1->val<l2->val){
                ltemp->next = new ListNode(l1->val);
                l1 = l1->next;
                ltemp = ltemp->next;
            }else{
                ltemp->next = new ListNode(l2->val);
                l2 = l2->next;
                ltemp = ltemp->next;
            }
        }
        if(l1 != NULL)
            ltemp->next = l1;
        else
            ltemp->next = l2;
        return head->next;
    }
};
