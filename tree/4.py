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
        if self.root is None:
            self.root  = Node(data)
            return
        cur = self.root
        while True:
            if data < cur.data:
                if cur.left == None:
                    cur.left = Node(data)
                    return
                else:
                    cur = cur.left
            else:
                if cur.right == None:
                    cur.right = Node(data)
                    return
                else:
        
                     cur = cur.right
    def getSmallest(self, root):
        cur = root
        while cur.left:
            cur = cur.left
        return cur


    def delete(self,root, data):
        if not root:
            print("Error! Not Found DATA")
            return root
                    
        if data<root.data: 
            root.left = self.delete(root.left, data)
            return root
        elif data > root.data:
            root.right = self.delete(root.right, data)
            return root
    
        if not root.left:
            temp = root.right
            del root
            return temp 
        elif not root.right:
            temp = root.left
            del root
            return temp 
        
        new = self.getSmallest(root.right)
        root.data = new.data
        root.right = self.delete(root.right, new.data)
        return root
                
def printTree( node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split(",")
for i in inp:
    c,v = i.split(" ")
    v = int(v)
    if c == 'i':
        print(f'insert {v}')
        T.insert(v)
    elif c == 'd':
        print(f'delete {v}')
        T.root = T.delete(T.root,v)
    printTree(T.root)
           
