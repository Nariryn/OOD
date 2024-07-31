class Queue:
    def __init__(self, ls = None):
        if ls is None:
            self.items = []
        else:
            self.items = ls
            
    def enqueue (self, data):
        self.items.append(data)
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)
        
    def is_empty(self):
        return len(self.items) == 0

    def __len__ (self):
        return len(self.items)
    
q = Queue()

inp = input("Enter Input : ").split(",")

q_remove = []
for cmd in inp:
    if cmd[0] == "E":
        cmd_type, value = cmd.split(' ')
        q.enqueue(value)
        output_str = ', '.join(q.items)
        print(output_str)
    elif cmd[0] == "D":
        if len(q) >= 1:
            value = q.dequeue()
            q_remove.append(value)
            output_str = ', '.join(q.items)
            if q.is_empty():
                output_str = "Empty"
            output_str = f"{value} <- {output_str}"
            print(output_str)
            continue
        print("Empty")
        
q_str = ', '.join(q.items)
q_remove_str = ', '.join(q_remove)
if not q.items:
    q_str = "Empty"
if not q_remove:
    q_remove_str = "Empty"
print(f"{q_remove_str} : {q_str}")