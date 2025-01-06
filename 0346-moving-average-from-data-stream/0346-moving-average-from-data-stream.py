#use list: runtime:O(n)cuz each list.pop(0)require moving rest of the elements in the list; space compelxity:O(size) 
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.list =[]
        self.window_sum =0

    def next(self, val: int) -> float:
        self.list.append(val)
        self.window_sum+= val 
        if len(self.list)> self.size:
            self.window_sum-=self.list.pop(0)
        return self.window_sum/len(self.list)
        
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)