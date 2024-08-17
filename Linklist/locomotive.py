class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
            self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp


    def sol(self):
        old = self.head
        temp = self.head
        while temp != None:
            if temp.data == 0 : 
                newhead = temp
                break
            temp = temp.next
        
        self.head = newhead
        temp = self.head
        while temp != None:
            if temp.next == None:
                temp.next = old
            elif temp.next.data == 0:
                temp.next = None
            temp = temp.next