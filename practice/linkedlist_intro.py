class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
class Linkedlist:
    def __init__(self, head = None):
        self.head = head
        
    def insert(self, value):
        node = Node(value)
        if self.head is Node:
            self.head = node
            return
        
        current_node = self.head
        
        while True:
            if current_node.next is None:
                current_node.next = node
                break
            current_node = current_node.next
            
    # def print_linkendlist(self):
    #     current_node = self.head
    #     while current_node is not None:
    #         print current_node.value '->',
    #         current_node = current_node.next