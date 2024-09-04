class Queue:
    def __init__(self, ls = None) -> None:
        if ls is None:
            self.item = []
        else:
            self.item = ls
            
    def enqueue(self, data):
        self.item.append(data)
        self.size += 1
        
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.item.pop(0)
        
    def is_empty(self):
        return len(self.item) == 0
    
    def size(self):
        len(self.size)
        
    