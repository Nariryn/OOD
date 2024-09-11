class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
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
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node
        self.size += 1
            
    def insert(self, i, data):
        new_node = Node(data)
        cur = self.head
        count = 0
        while cur is not None:
            if count == i:
                new_node.next = cur.next
                cur.next = new_node
                return
            cur = cur.next
            count += 1
        
    def deleteNode(self, key): 
         
        temp = self.head 

        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
        while(temp is not None): 
            if temp.data == key: 
                break
            prev = temp 
            temp = temp.next

        if(temp == None): 
            return
        prev.next = temp.next
 
        temp = None
 
    def pop(self):
        cur = self.head
        while cur.next is not None:
            temp = cur
            cur = cur.next
        temp.next = None
        self.size -= 1
        return cur.data

    def reverse(self):
        cur = self.head
        prev = None
        while cur is not None:
            new_node = cur.next
            cur.next = prev
            prev = cur
            cur = new_node
        self.head = prev
        
    def compare(self, list2):
        if self.size == list2.size:
            cur = self.head
            while cur is not None:
                list2.deleteNode(cur.data)
                cur = cur.next

            if list2.size == 0:
                return True
            else:
                return False
        else:
            return False
    
    def deleteAfter(self, i):
        cur = self.head
        count = 0
        while cur != None and cur.next != None:
            if count == i:
                delete_node = cur.next
                cur.next = delete_node.next
                delete_node = None
                return
            cur = cur.next
            count += 1
    
    def __str__(self):
        s = ""
        cur_node = self.head
        while cur_node is not None:
            s += str(cur_node.data) + " "
            cur_node = cur_node.next
        return s
    
    def nodeAt(self, i):
        cur = self.head
        for i in range(i):
            cur = cur.next
        return cur
    
List1 = Linkedlist()
List2 = Linkedlist()
List1.append(4)
List1.append(7)
List2.append(8)
List2.append(9)
List2.deleteNode(8)
print(List2)
print(List1.compare(List2))
print(List1.nodeAt(4))
# LL.pop()
# LL.reverse()
# print(LL)
        