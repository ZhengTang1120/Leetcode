class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q.append(x)

    # @return nothing
    def pop(self):
        self.q = self.q[0:-1]

    # @return an integer
    def top(self):
        return self.q[-1]

    # @return an boolean
    def empty(self):
        if len(self.q) == 0:
            return True
        else:
            return False