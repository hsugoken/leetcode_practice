"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #how to handle None? edge case
        #Will the node.random point to something always? 
        #if the input is None, what do we return here?
        #How are we given the input? Do we have the Node class with next and random?
        #Algo: we iterate through the node and create a copy of all the nodes
        #then we do a 2nd pass and connect the copy nodes? 
        #we maintain a map from original to copy using a hashmap
        copy_map = {None:None} #we map None to None
        cur = head
        while cur:
            #create a copy Node
            copy = Node(cur.val) 
            #map original to copy node
            copy_map[cur] = copy
            #move the linked list forward
            cur = cur.next
        cur = head
        while cur:
            #connect the next node
            copy_map[cur].next = copy_map[cur.next]
            #connect the random node
            copy_map[cur].random = copy_map[cur.random]
            #move cur fotward
            cur = cur.next

        return copy_map[head]



