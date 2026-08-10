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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
      int length=0;
      ListNode* lengthChecker=head;
      while (lengthChecker!=nullptr){
        length=length+1;
        lengthChecker=lengthChecker->next;
      }  
      if (length==1){
        return nullptr;
      }
      else if (length == n){
        return head->next;
      }
    
      lengthChecker=head;
      ListNode* prev=head;
      for (int i=0; i < length-n ;i++){
        prev=lengthChecker;
        lengthChecker=lengthChecker->next;
        
      }
     cout<<prev->val;
        cout<<lengthChecker->val;
      prev->next=lengthChecker->next;

      return head;
    }
};