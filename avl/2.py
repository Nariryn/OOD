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
                
def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)

def _findDiff(ptr,k,min_diff,min_diff_data):
    if ptr == None:
        return
    if ptr.data == k:
        min_diff_data[0] = k
        return
    if min_diff > abs(ptr.data - k):
        min_diff = abs(ptr.data - k)
        min_diff_data[0] = ptr.data

    if k < ptr.data:
        _findDiff(ptr.left,k,min_diff,min_diff_data)
    else:
        _findDiff(ptr.right,k,min_diff,min_diff_data)

def findDiff(root,k):
    min_diff, min_diff_data = 99999999999,[-1]
    _findDiff(root,k,min_diff,min_diff_data)
    return min_diff_data[0]

T = BST()
np,num = input('Enter Input : ').split("/")
inp = [int(i)for i in np.split()]
for i in inp:
    root = T.insert(i)
    printTree(T.root)
    print("--------------------------------------------------")
print(f'Closest value of {num} : {findDiff(T.root,int(num))}')