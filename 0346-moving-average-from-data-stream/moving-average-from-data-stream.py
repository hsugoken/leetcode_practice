class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = collections.deque([0]*(size))
        self.count = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.count += 1
        self.window.popleft()
        if self.count>self.size:
            self.count = self.size
        return sum(self.window)/self.count

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)