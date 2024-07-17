class Stack():

    def __init__(self, list=None):
        if list is None:
            self.items = []
        else:
            self.items = list
        self.current_size = len(self.items)

    def push(self, item):
        self.items.append(item)
        self.current_size += 1
        
    def pop(self):
        if not self.is_Empty():
            self.current_size -= 1
            return self.items.pop()
        else:
            return "Stack is empty"

    def is_Empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:
    s.push(e)

print(s.size(), "Data in stack : ", s.items)

while not s.is_Empty():
    s.pop()

print(s.size(), "Data in stack : ", s.items)
