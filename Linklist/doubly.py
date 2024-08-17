class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class Linkedlist:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None
    
    def append(self,item):
        newNode = Node(item)
        if self.head == None:
            self.head = self.tail = newNode
            return
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def revrse(self):
        if self.isEmpty():
            return "Empty"
        cur,s = self.tail, str(self.tail.value)+" "
        while cur.prev != None:
            s += str(cur.prev.value)+" "
            cur = cur.prev
        return s
    
    def size(self):
        if self.isEmpty():
            return 0 
        n = self.head
        i = 1
        while n.next != None:
            n = n.next
            i += 1 
        return i 
    
    def addHead(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n 

    def search(self,item):
        if self.isEmpty():
            return "Not Found"
        n = self.head
        i = 0
        while n.next != None:
            if n.value == item:
                return "Found"
            n = n.next
            i+=1
        if n.value == item:
            return "Found"
        return "Not Found"
        
    def index(self, item):
        if self.isEmpty():
            return -1
        n = self.head
        i = 0
        while n.next != None:
            if n.value == item:
                return i 
            n = n.next
            i+=1
        if n.value == item:
            return i 
        return -1
    
    def insert(self,pos,item):
        i = 1
        insert_n = Node(item)
        if pos < 0:
            pos = self.size() + pos
        if self.isEmpty():
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
        if pos >= self.size() or pos< 0:
            return "Out of Range"
        elif pos == 0:
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None
        elif pos == self.size() - 1:
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
