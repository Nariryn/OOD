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
        
        cur_node = self.root
        
        while True:
            if new_node.data < cur_node.data:
                if cur_node.left is None:
                    cur_node.left = new_node
                    break
                cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    cur_node.right = new_node
                    break
                cur_node = cur_node.right
                
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
def height(root):
    if root is None:
        return 0
    leftans = height(root.left)
    rightans = height(root.right)
    
    return max(leftans, rightans) + 1

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(T.root)

print("Height of the binary tree is: " + str(height(T.root)))