# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify result list construction
        add = ListNode()
        temp = add

        # Initialize carry for digit sums that exceed 9
        carry = 0

        # Loop through both linked lists until all digits and carry are processed
        while l1 or l2 or carry:
            # Get current digit values (0 if list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Compute total and update carry
            total = val1 + val2 + carry
            carry = total // 10
            total = total % 10

            # Append the current digit to the result list
            temp.next = ListNode(total)
            temp = temp.next

            # Move to the next nodes in both lists if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the result list starting from the next of dummy node
        return add.next

# Key Idea:
# Simulate the addition of numbers represented by linked lists digit-by-digit.
# Use carry to manage sums > 9, just like in manual addition.

# Edge Cases:
# 1. One list is longer than the other.
# 2. Carry remains after both lists are exhausted.
# 3. Both input lists are empty (return None or a 0-node depending on constraints).

# Time Complexity: O(max(N, M)) — where N and M are the lengths of the two lists.
# Space Complexity: O(max(N, M)) — for the output linked list.
