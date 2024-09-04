class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
        
class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def __str__(self) -> str:
        pass
        
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    
    def addHead(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def remove_head(self):
        if self.head == None:
            return
        self.head = self.head.next
        
    