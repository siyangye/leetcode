class MovingAverage:

    def __init__(self, size: int):
        self.queue=deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum+=val
        if len(self.queue)<=self.size:
            return self.sum/len(self.queue)
        else:
            self.sum-=self.queue.popleft()
            return self.sum/len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)