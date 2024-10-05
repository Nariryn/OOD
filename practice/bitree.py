class Node:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right

    def __str__(self) -> str:
        s = str(self.data)
        return s

class BST:
    def __init__(self,root = None) -> None:
        self.root = None if root is None else root
    
    def add(self,data):
        self.root = BST._add(self.root,data)

    def _add(root,data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left,data)
            else:
                root.right = BST._add(root.right,data)
        return root
    
    def addd(root,data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST.addd(root.left,data)
            else:
                root.right = BST.addd(root.right,data)
        return root
    def levelOrder(self):
        q = []
        q.append(self.root)
        while q:
            n = q.pop(0)
            print(n.data,end=' ')
            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)
    
    def _inOrder(root):
        if root is not None:
            BST._inOrder(root.left)
            print(root,end = ' ')
            BST._inOrder(root.right)
    
    def inOrder(self):
        BST._inOrder(self.root)

    def _preOrder(root):
        if root is not None:
            print(root,end = ' ')
            BST._preOrder(root.left)
            BST._preOrder(root.right)
    
    def preOrder(self):
        BST._preOrder(self.root)

    def _postOrder(root):
        if root is not None:
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root,end = ' ')
    
    def postOrder(self):
        BST._postOrder(self.root)

    def _deleteNodeP(root:Node,key:int) :
        if root is None: return root
        if int(key) < int(root.data):
            root.left = BST._deleteNodeP(root.left,key)
        elif int(key) > int(root.data):
            root.right = BST._deleteNodeP(root.right,key)
        else :
            if root.left is None or root.right is None:
                root = root.left if root.right is None else root.right
            else:
                temp = root.left
                while temp.right is not None :
                    temp = temp.right
                root.data = temp.data
                root.left = BST._deleteNodeP(root.left,temp.data)
        return root
    
    def deleteNode(self, data):
        self.root = BST._deleteNodeP(self.root, data)
