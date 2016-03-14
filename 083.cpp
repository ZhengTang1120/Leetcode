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
    ListNode *deleteDuplicates(ListNode *head) {
        if(head == NULL)
            return NULL;
        if(head->next == NULL)
            return head;
        vector<int> list;
        list.push_back(head->val);
        while(head->next){
            head = head->next;
            bool flag = true;
            for(int i = 0;i < list.size();i++){
                if(head->val == list[i]){
                    flag = false;
                    break;
                }
            }
            if(flag)
                list.push_back(head->val);
        }
        ListNode *re = new ListNode(list[0]);
        ListNode *p = re;
        for(int j = 1;j < list.size();j++){
            re->next = new ListNode(list[j]);
            re = re->next;
        }
        return p;
    }
};