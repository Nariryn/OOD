class Stack:
    def __init__(self, ls = None):
        if ls is None:
            self.items = []
        else:
            self.items = ls
        self.cur_size = len(self.items)
        
            
    def push(self, data):
        self.items.append(data)
        self.cur_size += 1
    
    def pop(self):
        if not self.is_Empty():
            self.cur_size -= 1
            return self.items.pop()
        else:
            return "Empty"
            
    def is_Empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter input : ").split()]

s = Stack()

for e in ls:
    s.push(e)

print(s.size(), "Data in  stack : ", s.items)

while not s.is_Empty():
    s.pop()
print(s.size(), "Data in  stack : ", s.items)