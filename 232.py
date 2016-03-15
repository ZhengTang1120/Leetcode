class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.instack = []
        self.outstack = []
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.instack.append(x)
        
    # @return nothing
    def pop(self):
        if len(self.outstack)!=0:
            self.outstack.pop()
        else:
            while len(self.instack)!=0:
                s = self.instack.pop()
                self.outstack.append(s)
            self.outstack.pop()

    # @return an integer
    def peek(self):
        if len(self.outstack)!=0:
            return self.outstack[-1]
        else:
            while len(self.instack)!=0:
                s = self.instack.pop()
                self.outstack.append(s)
            return self.outstack[-1]

    # @return an boolean
    def empty(self):
        if len(self.outstack)==0 and len(self.instack)==0:
            return True
        else:
            return False