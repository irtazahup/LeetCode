/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {

        ListNode* tail = head;
        int length = 1;
        
         if (head==nullptr || head->next==nullptr){
            return head;
        }

        while (tail->next != nullptr) {
            tail = tail->next;
            length++;
        }
        
        // Step 2: Handle cases where k >= length
        k = k % length;

        if (k == 0) {
            return head; // No rotation needed
        }
        
        // while (tail->next!=nullptr){
        //     tail=tail->next;
        // }
        // cout<<tail->val;
       

        while (k > 0){
            ListNode* prev=nullptr;
            tail=head;
            while (tail->next!=nullptr){
                prev=tail;
                tail=tail->next;
            }

            tail->next=head;
            head=tail;
            prev->next=nullptr;

            k=k-1;
        }

        return head;
        

    }
};