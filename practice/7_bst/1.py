class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        cur = self.root
        while True:
            if new_node.data < cur.data:
                if cur.left is None:
                    cur.left = new_node
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = new_node
                    break
                cur = cur.right
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
            
    def reverse(self, node):
        if node is None:
            return None
        
        node.left, node.right = node.right, node.left
        
        self.reverse(node.left)
        self.reverse(node.right)
        
        return node
        
    def Min(self):
        cur = self.root
        while cur.left != None:
            cur = cur.left
        min = cur.data
        return min
    
    def Max(self):
        cur = self.root
        while cur.right != None:
            cur = cur.right
        max = cur.data
        return max
    
    def preorder(self, node):
        if node is None:
            return
        print(node, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
    
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)
    
    def postorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        self.inorder(node.right)
        print(node.data, end=" ")
            
def height(node):
    if node is None:
        return 0
    leftans = height(node.left)
    rightans = height(node.right)
    
    return  max(leftans, rightans) + 1

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(T.root)
temp = height(T.root)
print(f"Height {temp}")
# re_inp = T.reverse(T.root)
# print(f"reverse {T.printTree(re_inp)}")
min_inp = T.Min()
print (f"Min : {str(min_inp)}")
T.preorder(T.root)
print("\n")
T.inorder(T.root)
T.postorder(T.root)
