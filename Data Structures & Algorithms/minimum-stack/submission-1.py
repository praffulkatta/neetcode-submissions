class MinStack:

    def __init__(self):
        self.s = []
        self.mini = []
        

    def push(self, val: int) -> None:

        self.s.append(val)

        if not slef.mini:
            self.mini.append(val)
        else:
            self.mini.append(min(self.mini, val))
        

    def pop(self) -> None:
        self.s.pop()
        self.mini.pop()
        

    def top(self) -> int:
        slef.s[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
