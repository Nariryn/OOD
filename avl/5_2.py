class Node:

    def __init__(self, data): 

        self.data = data  

        self.left = None  

        self.right = None 

        self.level = None 



    def __str__(self):

        return str(self.data) 



class Tree:

    def __init__(self): 

        self.root = None

        self.num = 0



    def insert(self, val):  

        if self.root == None:

            self.root = Node(val)

            self.num += 1

        else:

            h = height(self.root)

            max_node = pow(2,h+1)-1

            current = self.root

            if self.num+1 > max_node:

                while(current.left != None):

                    current = current.left

                current.left = Node(val)

                self.num+=1

            elif self.num+1 == max_node:

                while(current.right != None):

                    current = current.right

                current.right = Node(val)

                self.num+=1

            else:

                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)

                else:

                    insert_subtree(current.right,self.num - pow(2,h),val)

                self.num+=1

                    

def insert_subtree(r,num,val):

    if r != None:

        h = height(r)

        max_node = pow(2,h+1)-1

        current = r

        if num+1 > max_node:

            while(current.left != None):

                current = current.left

            current.left = Node(val)

            return

        elif num+1 == max_node:

            while(current.right != None):

                current = current.right

            current.right = Node(val)

            return

        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

            insert_subtree(current.left,num - round(pow(2,h)/2),val)

        else:

            insert_subtree(current.right,num - pow(2,h),val)

    else:

        return



def height(root):

    if root == None:

        return -1

    else:

        left = height(root.left)

        right = height(root.right)

        if left>right:

            return left + 1

        else:

            return right + 1

                       

def printTree90(node, level = 0):

    if node != None:

        printTree90(node.right, level + 1)

        print('     ' * level, node)

        printTree90(node.left, level + 1)

def maxValue(root):
    if root is None:
        return 0
    
    leftMax = maxValue(root.left)
    rightMax = maxValue(root.right)

    value = 0
    if leftMax > rightMax:
        value = leftMax
    else:
        value = rightMax
    
    if value < root.data:
        value = root.data
    
    return value

def minValue(root):
    if root is None:
        return 1000000000
    
    leftMax = minValue(root.left)
    rightMax = minValue(root.right)

    value = 0
    if leftMax < rightMax:
        value = leftMax
    else:
        value = rightMax

    if value > root.data:
        value = root.data
    
    return value

def isBST(root):
    if root is None:
        return True
    if (root.left is not None and maxValue(root.left)>=root.data):
        return False
    if (root.right is not None and minValue(root.right)<=root.data):
        return False
    if(isBST(root.left) is False or isBST(root.right) is False):
        return False
    return True

tree = Tree()

data = input("Enter Input : ").split()
check = 1
for e in data:
    tree.insert(int(e))
    if 0 > int(e) or int(e) > 100:
        check = 0

printTree90(tree.root)
if check:
    print(isBST(tree.root))
else:
    print(False)