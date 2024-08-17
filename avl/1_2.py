class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.minute = 0
    
    def __repr__(self) -> str:
        return str(self.data)
    
class AVL:
    def __init__(self):
        self.root = None
    
    def getHeight(self,root):
        if root is None:
            return 0
        
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        if left > right:
            value = left
        else:
            value = right
        
        return value + 1

    def getBalance(self,root):
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def leftRotate(self,root):
        y = root.right
        root.right = y.left
        y.left = root
        return y
    
    def rightRotate(self,root):
        x = root.left
        root.left = x.right
        x.right = root
        return x

    def _insert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left,data)
        else:
            root.right = self._insert(root.right,data)
        
        bf = self.getBalance(root)
        if bf > 1:
            lbf = self.getBalance(root.left)
            if lbf >= 0:
                return self.rightRotate(root)
            elif lbf < 0:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        
        elif bf < -1:
            rbf = self.getBalance(root.right)
            if rbf > 0 :
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
            elif rbf <= 0:
                return self.leftRotate(root)
        
        return root
    
    def insert(self,data):
        self.root = self._insert(self.root,data)

    def printTree(self, root: Node, level = 0):
        if root is not None:
            self.printTree(root.right, level + 1)
            print("    " * level, root)
            self.printTree(root.left, level + 1)

    def getNode(self,root,data):
        if root is None:
            return None
        if data < root.data:
            return self.getNode(root.left,data)
        elif data > root.data:
            return self.getNode(root.right,data)
        else:
            return root
    
    def getParent(self,root,node):
        if node is None or node == self.root:
            return None
        if root.left == node or root.right == node:
            return root
        if node.data < root.data:
            return self.getParent(root.left, node)
        else:
            return self.getParent(root.right, node)
        
    def burn(self,root):
        minute = 0
        q = []
        visited = []
        q.append(root)
        while len(q) > 0:
            node = q.pop(0)
            visited.append(node)
            if node.left is not None and node.left not in visited:
                temp = node.left
                temp.minute = node.minute + 1
                q.append(temp)
            if node.right is not None and node.right not in visited:
                temp = node.right
                temp.minute = node.minute + 1
                q.append(temp)
            parent = self.getParent(self.root,node)
            if parent is not None and  parent not in visited:
                parent.minute = node.minute + 1
                q.append(parent)
            minute += 1

        minute = 0
        for each in visited:
            if each.minute > minute:
                minute = each.minute
                print('')
            print(each, end=" ")
            

inp = input("Enter node and burn node : ").split('/')
burnnode = inp[1]
inp = inp[0].split()
if burnnode not in inp:
    print(f"There is no {burnnode} in the tree.")
    exit()

tree = AVL()
for i in inp:
    tree.insert(int(i))

burnnode = tree.getNode(tree.root, int(burnnode))
tree.burn(burnnode)