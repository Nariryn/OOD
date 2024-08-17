class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
        self.height = self.setHeight()
    
    def __str__(self) -> str:
        return str(self.data)
    
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height

    def getHeight(self, node):
        return -1 if node == None else node.height
    
    def balanceValue(self):
        return self.getHeight(self.left) - self.getHeight(self.right)
    
class AVL:
    def __init__(self,root = None):
        self.root = None if root is None else root
    
    def leftRotage(self,x):
        y = x.left
        x.left = y.right
        y.right = x
        x = y 
        x.right.setHeight()
        x.setHeight()
        return x
    
    def rightRotage(self,x):
        y = x.right
        x.right = y.left
        y.left = x
        x = y
        x.left.setHeight()
        x.setHeight()
        return x
    
    def rebalances(self,x):
        if x == None:
            return x
        balance = x.balanceValue()
        if balance == -2:
            if x.right.balanceValue() == 1:
                x.right = self.leftRotage(x.right)
            x = self.rightRotage(x)
        elif balance == 2:
            if x.left.balnceValue() == -1:
                x.left = self.rightRotage(x.left)
            x = self.leftRotage(x)
        x.setHeight()
        return x
        