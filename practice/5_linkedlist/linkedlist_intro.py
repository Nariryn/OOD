class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
            
    def __str__(self) -> str:
        return str(self.data)
            
class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            
            cur_node.next  = new_node
        self.size += 1
        
    
    def insert_index(self, data, index):
        idx = 0
        new_node = Node(data)
        if index >= self.size:
            return 
        cur_node = self.head
        while cur_node != None:
            if idx == index - 1:
                break
            cur_node = cur_node.next
            idx += 1
        new_node.next = cur_node.next
        cur_node.next = new_node
        self.size += 1
        
    def size(self):
        return self.size
    
    def __str__(self) -> str:
        s = ""
        cur_node = self.head
        while cur_node != None:
            s += str(cur_node) + " "
            cur_node = cur_node.next
        return s
    
    
    
            
LL = Linkedlist()
LL.append(3)
LL.append(2)
LL.append(5)
print(LL)