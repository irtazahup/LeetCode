// You are given the heads of two sorted linked lists list1 and list2.

// Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

// Return the head of the merged linked list.




# /**
#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     ListNode *next;
#  *     ListNode() : val(0), next(nullptr) {}
#  *     ListNode(int x) : val(x), next(nullptr) {}
#  *     ListNode(int x, ListNode *next) : val(x), next(next) {}
#  * };
#  */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* newhead=nullptr;
        ListNode* trivhead=nullptr;
        while (list1!=nullptr && list2 !=nullptr){
            if (list1->val < list2->val || list1->val == list2->val){
                if (newhead == nullptr){
                    newhead=list1;
                    trivhead=newhead;
                    list1=list1->next;
                }
                else{
                    trivhead->next=list1;
                    trivhead=list1;
                    list1=list1->next;
                }

            }
            else{
                if (newhead == nullptr){
                    newhead=list2;
                    trivhead=newhead;
                    list2=list2->next;
                }
                else{
                    trivhead->next=list2;
                    trivhead=list2;
                    list2=list2->next;
                }
            }
        }
        if (list1!=nullptr){
            while (list1!=nullptr){
                if (trivhead==nullptr){
                    trivhead=list1;
                    newhead=trivhead;
                }
                else{
trivhead->next=list1;
                 trivhead=list1;
               }
                list1=list1->next;
            }
        }
        // while (list2!=nullptr){
        //     cout << list2->val;
        //     list2=list2->next;
        // }

        if (list2!=nullptr){
            while (list2!=nullptr){
                if (trivhead== nullptr){
                trivhead=list2;
                newhead=trivhead;
                
                }
                else{
                    // cout<<list2->val;
                    // cout<<trivhead->val;
                    trivhead->next=list2;
                    trivhead=list2;
                    cout<<trivhead->val;
                    
               
                }
                list2=list2->next;
            }
        }

        return newhead;
    }
};