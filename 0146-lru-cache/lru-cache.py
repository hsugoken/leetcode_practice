"""
init with capacity
get(key) => returns value of key if it exists else -1
put(key,value) => updates the value of key if key exists else add key-value pair
                  to the cache
                  if #keys > capcaity => remove least recent
get O(1) => finding => hashmap (if found remove from current and add to tail)
put O(1) => addition + deletion => O(1) LL if we know the location
(least recent) head -> 1 <-> 2 <-> 3 <->4 <-> tail (most recent) 
{k1:Node(1), k2:Node(2),k3:Node(3) and k4:Node(4)}

"""
class ListNode:
    def __init__(self,key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.keymap = {}
        self.capacity = capacity

        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not key in self.keymap:
            return -1
        
        cur_node = self.keymap[key]
        self._remove(cur_node)
        self._add(cur_node)
        
        return cur_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keymap:
            # old_node = 
            self._remove(self.keymap[key])
        new_node = ListNode(key, value)
        self.keymap[key] = new_node
        self._add(new_node)

        if len(self.keymap)>self.capacity:
            least_node = self.head.next
            self._remove(least_node)
            del self.keymap[least_node.key]
        


    def _add(self, node):
        tail_prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = tail_prev
        tail_prev.next = node

    
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)