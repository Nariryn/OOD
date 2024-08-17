class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def creatTree(self,inp):
        stack = []
        for ch in inp:
            if ch in "+-*/":
                sec = stack.pop()
                first = stack.pop()
                new_node = Node(ch)
                new_node.left = first
                new_node.right = sec
                stack.append(new_node)
            else:
                stack.append(Node(ch))
        self.root = stack.pop()
    
def printTree( node, level = 0):
        if node != None:
            printTree(node.right, level + 1)
            print('     ' * level, node)
            printTree(node.left, level + 1)

def printInfix(root):
    if not root.left and not root.right:
        return root.data
    res = "("
    res += printInfix(root.left)
    res += root.data
    res += printInfix(root.right)
    res += ")"
    return res

def printPrefix(root):
    if not root:
        return ""
    res = ""
    res += root.data
    res += printPrefix(root.left)
    res += printPrefix(root.right)
    return res

T = BST()
inp = input("Enter Postfix : ")
T.creatTree(inp)
print("Tree :")
printTree(T.root)
print("--------------------------------------------------\n",end="")
print(f'Infix : {printInfix(T.root)}')
print(f'Prefix : {printPrefix(T.root)}')