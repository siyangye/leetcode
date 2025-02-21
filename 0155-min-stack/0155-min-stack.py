class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #update minstack: 
        if self.minstack: #not empty 
            minVal = min(val, self.minstack[-1]) #compare 
            self.minstack.append(minVal) 
        
        else: #empty
            self.minstack.append(val) #append val 
        
    def pop(self) -> None:
        self.stack.pop()
        #delete min:
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()