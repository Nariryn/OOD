class Queue:
    def __init__(self, ls = None):
        if ls is None:
            self.queue = []
        else:
            self.queue = ls
        
    def enqueue (self, data):
        self.queue.append(data)
    
    def dequeue (self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)
        
    def is_empty(self):
        return len(self.queue) == 0
        
    def __len__ (self):
        return len(self.queue)
    
q = Queue()
inp = input("Enter Input : ").split(",")

q_remove = []
for cmd in inp:
    if cmd[0] == "E":
        cmd_type, value = cmd.split(' ')
        q.enqueue(value)
        output_str = ', '.join(q.queue)
        print(output_str)  
    elif cmd[0] == "D":
        if len(q) >=1:
            value = q.dequeue()
            q_remove.append(value)
            output_str = ', '.join(q.queue)
            if q.is_empty():
                output_str = "Empty"
            output_str = f"{value} <- {output_str}"
            print(output_str)
            continue
        print("Empty")

q_str = ', '.join(q.queue)
q_remove_str = ', '.join(q_remove)
if not q.queue:
    q_str = "Empty"
if not q_remove:
    q_remove_str = "Empty"
print(f"{q_remove_str} : {q_str}")



# Testcase : #1
# Enter Input : E 1,E 2,E 3,D,D,E 4
# 1
# 1, 2
# 1, 2, 3
# 1 <- 2, 3
# 2 <- 3
# 3, 4
# 1, 2 : 3, 4

# Testcase : #2
# Enter Input : E 1,E 2,D,D,D
# 1
# 1, 2
# 1 <- 2
# 2 <- Empty

# Testcase : #3
# Enter Input : D
# Empty
# Empty : Empty