class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if not self.stack:
            return
        while len(self.stack) > 1:
            self.temp_stack.append(self.stack.pop())
        #len(stack) == 1: 
        pop_int = self.stack.pop()
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())
        return pop_int

    def peek(self) -> int:
        if not self.stack:
            return
        return self.stack[0]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()