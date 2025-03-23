class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.num_list = []
        

    def insert(self, val: int) -> bool:
        if val not in self.num_map:
            res = True
        else:
            res = False
        if res:
            self.num_map[val] = len(self.num_list)
            self.num_list.append(val)
        return res
        

    def remove(self, val: int) -> bool:
        res = val in self.num_map
        if res:
            idx = self.num_map[val] #get index of value
            last_value = self.num_list[-1]
            #move last_value to index
            self.num_list[idx] = last_value
            #update the hashmap
            self.num_map[last_value] = idx
            #now remove the last value 
            self.num_list.pop() #remove from list
            del self.num_map[val] #remove from hashmap
        return res

    def getRandom(self) -> int:
        return random.choice(self.num_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()