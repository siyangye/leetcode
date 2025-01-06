#use deque :runtime complexity: O(1)
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.list = deque()
        self.sums = 0

    def next(self, val: int) -> float:
        self.list.append(val)
        self.sums += val
        if len(self.list)> self.size:
            self.sums-=self.list.popleft()
        return self.sums/len(self.list)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)