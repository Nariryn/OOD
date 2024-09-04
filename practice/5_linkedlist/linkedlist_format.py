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
            self.head = self.tail = new_node   
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
                
            cur.next = new_node
            self.tail = cur.next
        self.size += 1   
            
    def removeTail(self):
        pass
    
    def insert_index(self, data, index):
        idx = 0
        new_node = Node(data)
        
        if index >= self.size:
            return
        
        cur = self.head
        while cur is not None:
            if idx == index - 1:
                break
            cur = cur.next
            idx += 1
            
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1
    
    def size(self):
        return self.size
    
    def __str__(self) -> str:
        s = ""
        cur = self.head
        while cur is not None:
            s += str(cur.data) + " "
            cur = cur.next
        return s
    
    def reverse(self):
        cur_node = self.head
        prev  = None
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next_node
        return prev
    
LL = Linkedlist()
LL.append(1)
LL.append(2)
LL.append(3)
LL.insert_index(4,1)
LL.reverse()
print(LL)
        