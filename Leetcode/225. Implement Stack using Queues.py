
class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if not self.q1:
            return None
        # Move all but last element from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        # This is the last pushed item (i.e., top of the stack)
        val = self.q1.popleft()
        # Swap queues
        self.q1, self.q2 = self.q2, self.q1
        return val

    def top(self):
        if not self.q1:
            return None
        # Move all but last element from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        # Peek at last item
        val = self.q1[0]
        self.q2.append(self.q1.popleft())  # move last item too
        # Swap queues
        self.q1, self.q2 = self.q2, self.q1
        return val

    def empty(self):
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
