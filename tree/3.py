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

    def maxPath(self):
        return self._maxPath(self.root)[1]

    def _maxPath(self, root):
        if not root:
            return 0, []

        lv, ll = self._maxPath(root.left)
        rv, rl = self._maxPath(root.right)
        mv = max(lv, rv)
        if mv == lv:
            ml = ll
        else:
            ml  = rl
            
        return root.data+mv, [root.data] + ml

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)  

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

T = BST()
inp = [int(i) for i in input('Enter tree: ').split()]
for i in inp:
    T.newInsert(i)
print(f'Maximum path: {T.maxPath()}')