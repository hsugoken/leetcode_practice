"""
set capacity, head points to least recent tail points to most recent
get => returns value of key if present else -1 
put => updates value of key if present else adds key-value pair and checks for capacity and if it exceeds 
evicts the least recent
Algo: we will use a hashmap to map key -> Node in DLL, will give us O(1) time in get
For put using a DLL helps as we can insert and remove using a DLL in O(1) with the get 
"""
class DoublyLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.head = DoublyLinkedList(-1,-1) #least recent
        self.tail = DoublyLinkedList(-1,-1) #most recent
        #connecting the head and tail nodes
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.nodemap = {} #maps key->node

    def get(self, key):
        if key not in self.nodemap:
            return -1
        
        cur_node = self.nodemap[key]
        self._remove(cur_node)
        self._add(cur_node)
        return cur_node.val

    def put(self, key, value):
        if key in self.nodemap:
            old_node = self.nodemap[key]
            self._remove(old_node)
        new_node = DoublyLinkedList(key, value)
        self.nodemap[key] = new_node
        self._add(new_node)
        if len(self.nodemap)>self.cap:
            least_recent_node = self.head.next
            self._remove(least_recent_node)
            del self.nodemap[least_recent_node.key]

    def _add(self, node):
        #we add just before the tail node
        prev_node = self.tail.prev
        
        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node



    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        #connecting the previous and next node
        prev_node.next = next_node
        next_node.prev = prev_node
    