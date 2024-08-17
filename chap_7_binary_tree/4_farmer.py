class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def append(self, data):
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

    def cut(self, data):
        def cut_branch(node, data):
            if node is None:
                return None, False
            
            if node.data == data:
                if node.right:
                    node.right = None
                    return node, True
                elif node.left:
                    node.left = None
                    return node, True
                else:
                    return node, False
            
            if data < node.data:
                node.left, cut_flag = cut_branch(node.left, data)
            else:
                node.right, cut_flag = cut_branch(node.right, data)
            
            return node, cut_flag

        self.root, result = cut_branch(self.root, data)
        return result
    
    def preorder(self, node, stop):
        if node:
            if node.data > stop:
                print(node.data, end=' ')
            else:
                ascii_values = ''.join(str(ord(c)) for c in node.data)
                print(ascii_values, end=' ')
            self.preorder(node.left, stop)
            self.preorder(node.right, stop)

    def inorder(self, node, stop):
        if node:
            self.inorder(node.left, stop)
            if node.data > stop:
                print(node.data, end=' ')
            else:
                ascii_values = ''.join(str(ord(c)) for c in node.data)
                print(ascii_values, end=' ')
            self.inorder(node.right, stop)

    def postorder(self, node, stop):
        if node:
            self.postorder(node.left, stop)
            self.postorder(node.right, stop)
            if node.data > stop: 
                print(node.data, end=' ')
            else:
                ascii_values = ''.join(str(ord(c)) for c in node.data)
                print(ascii_values, end=' ')

            
    def printMirrorTree(self, node, level = 0):
        if node != None:
            self.printMirrorTree(node.left, level + 1)
            print('     ' * level, node)
            self.printMirrorTree(node.right, level + 1)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
print("What is this a plum tree")
first,inp = input('Enter Input : ').split('/')
first = first.split()
for i in first:
    T.append(i)
print("FIrst look of this plum tree")
T.printTree(T.root)
print("********************************************")
inp = inp.split(',')
for i in inp:
    print(i)
    if i[:2] == "AP":
        T.append(i[3:])
        T.printTree(T.root)
    elif i[:2] == "CU":
        result = T.cut(i[3:])
        if result is False:
            print("Not thing change")
        T.printTree(T.root)
    elif i[:2] == "CH":
        print('preorder  :',end=' ')
        T.preorder(T.root,i[3:])
        print('\ninorder   :',end=' ')
        T.inorder(T.root,i[3:])
        print('\npostorder :',end=' ')
        T.postorder(T.root,i[3:])
        print()
    elif i[:2] == "MI":
        T.printMirrorTree(T.root)
    print("********************************************")
print("the last result")
T.printTree(T.root)