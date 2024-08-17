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

    def newInsert(self, data):
        node = Node(data)
        if not self.root:
            self.root = node
            return
        q = [self.root]
        while q: 
            cur = q.pop(0)
            if not cur.left:
                cur.left = node
                return
            elif not cur.right:
                cur.right = node
                return 
            q.append(cur.left)
            q.append(cur.right)

    

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)  

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.newInsert(i)
T.printTree(T.root)