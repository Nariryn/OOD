class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node_data):
        new_node = Node(node_data)
        
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
    
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def three_time(self, num, k, node):
        if node is None:
           return
            
        if node.data > k:
            node.data *= num
            
        self.three_time(num, k, node.left)
        self.three_time(num, k, node.right)

T = BST()
inp = input('Enter Input : ').split("/")
inp_tree = [int(i) for i in inp[0].split()]
inp_k = int(inp[1])
for i in inp_tree:
    T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------")
num = 3
k = inp_k
T.three_time(num, k, node = T.root)
T.printTree(T.root)