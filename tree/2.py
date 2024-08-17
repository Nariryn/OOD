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
                
    def maxDepth(self,node):
        if node is None:
            return 0
        else:
            ldepth = self.maxDepth(node.left)
            rdepth = self.maxDepth(node.right)

            if (ldepth > rdepth):
                return ldepth+1
            else:
                return rdepth+1

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print(f'Height of this tree is : {T.maxDepth(T.root)-1}')