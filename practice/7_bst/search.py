class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.key)

class BST:
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, key):
        new_node = Node(key)
        
        if not self.root:
            self.root = new_node
            return
        
        cur_node = self.root
        
        while True:
            if new_node.key < cur_node.key:
                if cur_node.left is None:
                    cur_node.left = new_node
                    break
                cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    cur_node.right = new_node
                    break
                cur_node = cur_node.right
                
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        
        if root.key < key:
            return self.search(root.right, key)
        
        return self.search(root.left, key)
    
T = BST()
inp = list(map(int, input("Enter Input : ").split()))
for i in inp:
    T.insert(i)
num = 15
if T.search(T.root, num):
    print("Found")
else:
    print("Not Found")
    