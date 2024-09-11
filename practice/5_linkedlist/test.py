class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is not None:
            return self.next is None
        else:
            self.next = next
            
class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
        self.size += 1
        
    def remove(self, items):
        if self.head is None:
            print ("Empty")
            return 
        cur = self.head
        if self.head.data == items:
            self.head = self.head.next
            return
        while cur is not None:
            if cur.data == items:
                break
            prev = cur
            cur = cur.next 
        if cur is None:
            print ("Empty")
        else:
            cur = prev        
            
        
            
        
        