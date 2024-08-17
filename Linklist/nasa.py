class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None :
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def remove(self):
        self.tail = self.tail.prev

    def reverse(self):
        h = self.head
        while h is not None:
            h.prev, h.next = h.next, h.prev
            h = h.prev
        self.head, self.tail = self.tail, self.head

    def print_list(self):
        h = self.head
        while h.next is not None:
            print(h.value, end=' -> ')
            h = h.next
        print(h.value)
    
    def backward(self):
        t = self.tail
        return t.prev

l = DoubleLinkedList()
p = DoubleLinkedList()
lastpage = None
b = None
inp = input("Enter Input : ").split(",")
for i in inp:
    if i[0] == "E":
        data = i.split(" ")[1]
        l.append(data)
        if p.head == None and data == "ce.kmitl.ac.th":
            pass
        else:
            p.append(data)
        b = None
    elif i[0] == "B":
        if b == None:
            b = l.backward()
        else:
            b = b.prev
        if b is not None:
            lastpage = b.next
            l.append(b.value)
            p.remove()
    elif i[0] == "F":
        if lastpage != None:
            l.append(lastpage.value)
            p.append(lastpage.value)
            b = None
print("History : ",end="")
l.print_list()
p.reverse()
print("BackPath : ",end="")
p.print_list()