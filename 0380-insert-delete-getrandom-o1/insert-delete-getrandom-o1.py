class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap #True if val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList) #adding numMap in the last index
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            idx = self.numMap[val] #index to remove value from
            lastVal = self.numList[-1]
            #move lastVal to idx 
            self.numList[idx] = lastVal
            self.numMap[lastVal] = idx
            #delete the val from numMap and numList
            self.numList.pop()
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()