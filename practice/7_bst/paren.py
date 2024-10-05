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

def parent(root, data):
    if int(root.data) == int(data):
        return "none because " + str(data) + " is the root"
    cur = root
    while True:
        if cur.left != None and int(cur.left.data) == int(data):
            return cur.data
        elif cur.right != None and int(cur.right.data) == int(data):
            return cur.data
        elif int(data) < int(cur.data):
            if cur.left == None:
                return "not found"
            else:
                cur = cur.left
        elif int(data) > int(cur.data):
            if cur.right == None:
                return "not found"
            else:
                cur = cur.right
                

T = BST()
data, inp_num = input("Enter Input : ").split("/")
data_lst = list(map(int, data.split()))
for i in data_lst:
    T.insert(i)
T.printTree(T.root)
is_parent = parent(T.root, inp_num)
print(f"parent of {inp_num} is {is_parent} ")