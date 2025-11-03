# Last updated: 11/2/2025, 8:23:39 PM
class MinStack:

    def __init__(self):
        self.minStack = [] #Main stack to store all values
        self.stack = [] #Auxilliary stack to store current minimums

    def push(self, val: int) -> None:
        self.stack.append(val) #push val to main stack 
        #If the minStack is not empty
        if self.minStack:
            #Push the smaller of the current value and the current minimum onto the minStack
            self.minStack.append(min(val, self.minStack[-1])) 
        else: #If the minStack is empty 
            self.minStack.append(val) #first value becomes the min 
        

    def pop(self) -> None:
        self.stack.pop() #Pop from main stack
        self.minStack.pop() #Pop from min stack


    def top(self) -> int:
        return self.stack[-1] #Return the top value of the main stack

    def getMin(self) -> int:
        return self.minStack[-1] #Return the current minimum (top of minStack)
    
    #Time: O(1) for all operations. 
    #Space: O(n) for storing elements in both stack and minStack.

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()