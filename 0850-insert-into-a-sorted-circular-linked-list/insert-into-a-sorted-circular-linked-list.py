"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            copy = Node(insertVal)
            copy.next = copy
            return copy
        cur = head
        while cur.next!=head:
            if cur.val<=insertVal<=cur.next.val:
                copy = Node(insertVal)
                copy.next = cur.next
                cur.next = copy
                return head
            if cur.val>cur.next.val:
                if cur.val<insertVal or insertVal<cur.next.val:
                    copy = Node(insertVal)
                    copy.next = cur.next
                    cur.next = copy
                    return head
            cur = cur.next
        copy = Node(insertVal)
        copy.next = cur.next
        cur.next = copy
        return head
        