class MinStack:

    def __init__(self):
        self.store = []
        self.min_store = []
        
    def push(self, val: int) -> None:
        self.store.append(val)
        # Edge Case 
        if len(self.min_store) == 0:
            self.min_store.append(val)
        else:    
            self.min_store.append(min(self.min_store[-1], val))

    def pop(self) -> None:
        self.store.pop()
        self.min_store.pop()

    def top(self) -> int:
        return self.store[-1]

    def getMin(self) -> int:
        return self.min_store[-1]
