class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self) -> str:
        if self.is_empty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    
    def reverse(self):
        if self.is_empty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.prev != None:
            s += str(cur.prev.value) + " "
            cur = cur.prev
        return s               
            
    def is_empty(self):
        return self.head == None
    
    def size (self):
        if self.is_empty():
            return 0
        n = self.head
        i = 1
        while n.next != None:
            n = n.next
            i += 1
        return i
    
    def append(self, item):
        n = Node(item)
        if self.is_empty():
            self.head = self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
            
    def addHead(self, item):
        n = Node(item)
        if self.is_empty():
            self.head = self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n
            
    def search(self, item):
        if self.is_empty():
            return "Not Found"
        n = self.head
        while n.next != None:
            if n.value == item:
                return "Found"
            n = n.next
        if n.value == item:
            return "Found"
        return "Not Found"
    
    def index(self, item):
        if self.is_empty():
            return -1
        n = self.head
        i = 0
        while n.next != None:
            if n.value == item:
                return i
            n = n.next
            i += 1
        if n.value == item:
            return i
        return -1
    
    def insert(self, pos, item):
        i = 1
        insert_n = Node(item)
        if pos < 0:
            pos = self.size() + pos
        if self.is_empty():
            self.head = self.tail = insert_n
        elif pos <= 0:
            self.addHead(item)
        elif pos >= self.size():
            self.append(item)
        else:
            n = self.head
            while n.next != None and i < pos:
                n = n.next
                i += 1
            insert_n.next = n.next
            insert_n.prev = n
            n.next.prev = insert_n
            n.next = insert_n
        return
    
    def pop(self, pos):
        i = 0
        if pos < 0:
            pos = self.size() + pos
        if pos >= self.size() or pos < 0:
            return "Out of Range"
        elif pos == 0:
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None
        elif pos == self.size() -1:
            self.tail = self.tail.prev
            if self.tail != None:
                self.tail.next = None
        else:
            n = self.head
            while n.next != None and i < pos:
                n = n.next
                i += 1
            n.next.prev = n.prev
            n.prev.next = n.next
        return "Success"
    
L = LinkedList()

inp = input("Enter Input : ").split(",")
for i in inp:
    #append
    if i[:2] == "AP":
        L.append(i[3:])
    #addhard
    elif i[:2] == "AH":
        L.addHead(i[3:])
    #search
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    #size
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    #index
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    #pop
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    #insert " " at postion " "
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
        
        
        