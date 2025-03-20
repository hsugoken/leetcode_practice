"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        """
          10->1-->2 <- Head
          ^        |
          |        v
         .9--------5
        target = 10
        """
        if not head:
            copy = ListNode(insertVal)
            copy.next = copy
            return copy
        
        cur = head
        while cur.next!=head:#cur =5
            if cur.val<=insertVal<=cur.next.val: 
                copy = ListNode(insertVal)
                
                copy.next = cur.next
                cur.next = copy
                return head
                #9>1 and 9<10 or 1>10
            if cur.val>cur.next.val and (cur.val<insertVal or cur.next.val>insertVal):
                copy = ListNode(insertVal)  #(10)
                
                copy.next = cur.next
                cur.next = copy
                return head
            cur = cur.next
        copy = ListNode(insertVal)
                
        copy.next = cur.next
        cur.next = copy

        return head

                
                
#T:O(N)
#S:O(1)