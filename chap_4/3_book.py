class Queue :
    def __init__(self, ls = None) -> None:
        if ls is None:
            self.queue = []
        else:
            self.queue = ls
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
    
    def len(self):
        return len(self.queue)
    
inp = input("Enter Input : ").split("/")
book = inp[0].split()
cmd = inp[1].split(",")

book_shelf = Queue(book)

for i in cmd:
    if i.startswith("E"):
        data, value = i.split()
        book_shelf.enqueue(value)
    elif i == "D":
        book_shelf.dequeue()

book_seen = set()
duplicate_found = False

for book in book_shelf.queue:
    if book in book_seen:
        duplicate_found = True
        break
    book_seen.add(book)
    
if duplicate_found:
    print ("Duplicate")
    
else:
    print ("NO Duplicate")
    
    
'''
Testcase student: #1
Enter Input : 1 2 7 2 4 6 8/E 5,D,D,E 1,E 3,D
NO Duplicate

Testcase student: #2
Enter Input : 1 1 1 1/E 2,E 3,D,D
Duplicate
'''