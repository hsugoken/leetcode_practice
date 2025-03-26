"""
Inserting and Removing a Value in O(1) done with hashset
getting random in O(1) cannot be done with hashset
O(1) random => needs a list
hashset => value -> index in list
Swapping with the last element to maintain O(1) time complexity
This avoids shifting elements which would be O(n)
"""
# [[],("insert",1),("remove",2),("insert",3), ("remove",3)]
#                                                ^
# x = RandomizedSet()
# x.num_list = [1]
# x.num_map = {1:0}
# Output: [null, True, False, True, False]

class RandomizedSet(object):

    def __init__(self):
        self.num_list = []
        self.num_map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        #returns True only when we need to insert a value
        res = val not in self.num_map #True if val not there
        if res:
            last_index = len(self.num_list) #0
            #insert value in list
            self.num_list.append(val)
            #insert value in hash_map
            self.num_map[val] = last_index
        return res
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        #returns true of item was present -> remvoves the value
        #key points: pop through list end in O(1)
        #del from hash_map
        res = val in self.num_map
        #[1,2,3]
        #2->1
        #3->2
        if res:
            last_val = self.num_list[-1]
            cur_val_idx = self.num_map[val]
            #update values and index
            self.num_list[cur_val_idx] = last_val
            self.num_map[last_val] = cur_val_idx
            #delete values
            self.num_list.pop()
            del self.num_map[val]
        return res

        

    def getRandom(self):
        """
        :rtype: int
        """
        #This does not handle duplicates
        if not self.num_list:
            return []
        else:
            return random.choice(self.num_list)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()