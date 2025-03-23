class RandomizedSet:

    def __init__(self):
        self.numMap = {} #{}
        self.numList = []#[]
    #insert [1]
    def insert(self, val: int) -> bool:
        #res = False
        res = val not in self.numMap #True if val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList) #adding numMap in the last index
            self.numList.append(val)
        return res #False
    #remove 1
    def remove(self, val: int) -> bool:
        res = val in self.numMap #True
        if res:
            idx = self.numMap[val] #index to remove value from #idx = 0
            lastVal = self.numList[-1] #1
            #move lastVal to idx 
            self.numList[idx] = lastVal #numList[0]=1
            self.numMap[lastVal] = idx #numMap = {1:0}
            #delete the val from numMap and numList
            self.numList.pop()# 
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
    
        return random.choice(self.numList)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()