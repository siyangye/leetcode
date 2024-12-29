class Solution:
    def calculate(self, s: str) -> int: # Initialize variables
        stack = []
        curr_num = 0
        curr_op = '+'  # Start with + to handle first number
        
        # Iterate through each character including an extra '+' at the end
        # to handle the last number
        i = 0
        string = s+ '+'
        for i in range(len(s+'+')):
        # for i, char in enumerate(s + '+'):
            char = string[i]
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            
            elif char != ' ':
                # Process the previous operator
                if curr_op == '+':
                    stack.append(curr_num)
                elif curr_op == '-':
                    stack.append(-curr_num)
                elif curr_op == '*':
                    stack.append(stack.pop() * curr_num)
                elif curr_op == '/':
                    # Handle division - be careful with negative numbers, cannot use a// b if a or b is negation, so we have to use int(a/b) to get the expected division result
                    prev_num = int(stack.pop()/curr_num)
                    stack.append(prev_num)
                
                # Update operator and reset current number
                curr_op = char
                curr_num = 0
        
        # Sum up all numbers in stack
        return sum(stack)
                