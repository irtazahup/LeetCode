class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0); // Dummy node to anchor the result list
        ListNode* tail = &dummy;
        int carry = 0;

        // Loop runs if there are digits left or a carry remaining
        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            int sum = carry;

            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }

            carry = sum / 10; // Calculate new carry
            
            // Allocate new node dynamically on the heap
            tail->next = new ListNode(sum % 10); 
            tail = tail->next; // Move tail forward
        }

        return dummy.next; // Return actual head of the new list
    }
};
