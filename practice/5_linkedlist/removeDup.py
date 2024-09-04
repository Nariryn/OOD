class Node:
    def  __init__(self, data, next = None):
        self.data = data
        if next is not None:
            self.next
        else:
            self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def append(self, data):
        new_node = Node(data)
        if self.haed == None:
            self.head == self.tail == new_node
        else:
            self.tail.next  = new_node
            self.tail = new_node
        self.size += 1

    def size(self):
        return self.size
    
    def str(self):
        result = []
        cur_node = self.head
        while cur_node is not None:
            result.append(str(cur_node.data))
            cur_node = cur_node.next
        return ' -> '.join(result)
        
    
    def  remove_dup(self):
        if self.head is None:
            return
        
        cur_node = self.head
        while cur_node is not None:
            runner = cur_node
            while runner.next is not None:
                if runner.next.data == cur_node.data:
                    runner.next = runner.next.next
                    self.size -= 1
                else:
                    runner = runner.next
            cur_node = cur_node.next
            
listdata1, listdata2 = input('List1, List2: ').split(', ')
listdata1 = listdata1.split(' ')
listdata2 = listdata2.split(' ')

list1 = LinkedList()
list2 = LinkedList()

for data in listdata1:
    list1.append(data)
for data in listdata2:
    list2.append(data)

# Removing duplicates
list1.remove_dup()
list2.remove_dup()

print('List1 after removing duplicates:', list1)
print('List2 after removing duplicates:', list2)
                    
'''
l1 = [1,1,2,2,3,3,4,4,5]
l2 = [1,2,3,4,5]

for i in l1:
    if i in l2:
        continue
    else:
        l2.append(i)
        
print(l2)


'''