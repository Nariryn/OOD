class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        
    def __str__(self):
        return str(self.data)
class AVLTree:
    def __init__(self):
        self.root = None
        
    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
        
    def insert(self, root, data):
        if not root:
            return root(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        
        balance = self.balance(root)
        
        # LL case
        if balance > 1 and data > root.left.data:
            pass
        
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
    def right_rotate(self, z):
        y = z.left
        T2 = y.right
        
        y.right = z