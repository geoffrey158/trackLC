# Last updated: 11/2/2025, 8:23:30 PM
class MyStack:

    def __init__(self):
        self.queue = collections.deque() 

    def push(self, x: int) -> None:
        q = self.queue
        q.append(x)
        #use _ since we don't actully need to use the variable
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self) -> int:
        #popleft means pop from the beginning of queue, since stack is the opoosite we use popleft
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not len(self.queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()