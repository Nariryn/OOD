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

class Queue:
    def __init__(self):
        self.queue = []
        self.dequeued = []

    def enqueue(self, data):
        self.queue.append(data)
        self.display()

    def dequeue(self):
        if self.is_empty():
            self.dequeued.append('Empty')
            print('Empty')
        else:
            removed = self.queue.pop(0)
            self.dequeued.append(removed)
            self.display(removed)

    def is_empty(self):
        return len(self.queue) == 0

    def display(self, removed=None):
        if removed is not None:
            print(f"{removed} <- " + (", ".join(map(str, self.queue)) if self.queue else "Empty"))
        else:
            print(", ".join(map(str, self.queue)) if self.queue else "Empty")

    def final_display(self):
        if self.is_empty():
            print("Empty")
        else:
            print(", ".join(map(str, self.queue)), end=' : ')
        print(", ".join(map(str, self.dequeued)))


myQueue = Queue()
inp = input("Enter Input : ").split(",")

for command in inp:
    if "E" in command:
        myQueue.enqueue(int(command.split()[1]))
    elif "D" in command:
        myQueue.dequeue()

myQueue.final_display()
