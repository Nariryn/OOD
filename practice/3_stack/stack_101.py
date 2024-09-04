class Stack:
    def __init__(self, ls = None):
        if ls is None:
            self.item = []
        else:
            self.item = ls
        self.size = len(self.item)
            
    def push(self, data):
        self.item.append(data)
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            self.item.pop()
            self.size -= 1
            
    def peek(self):
        return self.item[-1]
        
    def is_empty(self):
        return self.size() == 0
    
    def size(self):
        return self.size()
        
    
