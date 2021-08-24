class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sta = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.sta.append(val)
        if self.mins != [] :
            val = min(val, self.mins[-1])
            self.mins.append(val)
        else:
            self.mins.append(val)

    def pop(self) -> None:
        self.sta.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.sta[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()