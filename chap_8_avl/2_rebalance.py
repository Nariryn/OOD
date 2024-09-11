class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.value)


class AVL_Tree(object):
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        # Left-Left (LL) Case
        if balance > 1 and value < root.left.value:
            print("Not Balance, Rebalance!")
            return self.right_rotate(root)

        # Right-Right (RR) Case
        if balance < -1 and value > root.right.value:
            print("Not Balance, Rebalance!")
            return self.left_rotate(root)

        # Left-Right (LR) Case
        if balance > 1 and value > root.left.value:
            print("Not Balance, Rebalance!")
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left (RL) Case
        if balance < -1 and value < root.right.value:
            print("Not Balance, Rebalance!")
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y


def printTree90(node, level=0):
    if node is not None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


myTree = AVL_Tree()
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :", e)
    root = myTree.insert(root, int(e))
    printTree90(root)
    print("===============")
