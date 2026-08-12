from collections import deque

class MinStack:
    st = None
    def __init__(self):
        self.st = deque()

    def push(self, val: int) -> None:
        _min = val
        if self.st:
            _min = min(val, self.st[-1][1])
        self.st.append((val, _min))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
