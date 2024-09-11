class AVLNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

    def __str__(self):
        return str(self.data)

    def update_height(self):
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))

    @staticmethod
    def get_height(node):
        return node.height if node else 0

    def balance_factor(self):
        return self.get_height(self.right) - self.get_height(self.left)

class AVLTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        self.root = self._add(self.root, int(data))

    def _add(self, root, data):
        if not root:
            return AVLNode(data)
        
        if data < root.data:
            root.left = self._add(root.left, data)
        elif data > root.data:
            root.right = self._add(root.right, data)
        else:
            root.right = self._add(root.right, data)

        root.update_height()
        return self._balance(root)

    def _balance(self, root):
        if not root:
            return None

        balance = root.balance_factor()

        # Left Heavy
        if balance < -1:
            if root.left.balance_factor() <= 0:
                return self._rotate_right(root)
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)

        # Right Heavy
        if balance > 1:
            if root.right.balance_factor() >= 0:
                return self._rotate_left(root)
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        return root

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.update_height()
        y.update_height()

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.update_height()
        y.update_height()

        return y

    def post_order(self):
        print("AVLTree post-order :", end=' ')
        self._post_order(self.root)
        print()

    def _post_order(self, root):
        if root:
            self._post_order(root.left)
            self._post_order(root.right)
            print(root.data, end=' ')

    def print_tree(self):
        self._print_tree(self.root, 0)
        print()

    def _print_tree(self, node, level):
        if node:
            self._print_tree(node.right, level + 1)
            print('     ' * level, node.data)
            self._print_tree(node.left, level + 1)

avl = AVLTree()

inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AD":
        avl.add(i[3:])
    elif i[:2] == "PR":
        avl.print_tree()
    elif i[:2] == "PO":
        avl.post_order()