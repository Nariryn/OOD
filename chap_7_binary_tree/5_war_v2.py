class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left = None
        self.right = right = None

class BinarySearchTree:
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

    def delete_node(self, node):
        if node.left is None and node.right is None:
            self._replace_parent_reference(node, None)
        elif node.left is not None and node.right is not None:
            successor = self._find_min(node.right)
            node.data = successor.data
            self.delete_node(successor)
        else:
            child = node.left if node.left else node.right
            self._replace_parent_reference(node, child)

    def _replace_parent_reference(self, node, new_child):
        parent = self._get_parent(node)
        if parent is None:
            self.root = new_child
        elif parent.left == node:
            parent.left = new_child
        else:
            parent.right = new_child

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _get_parent(self, node, current_node=None):
        if current_node is None:
            current_node = self.root
        if current_node is None or current_node == node:
            return None
        if current_node.left == node or current_node.right == node:
            return current_node
        if node.data < current_node.data:
            return self._get_parent(node, current_node.left)
        return self._get_parent(node, current_node.right)

    def traverse_and_delete(self, node, condition, target_sum, current_path="", current_sum=0, deletion_index=0):
        if node is None:
            return deletion_index

        deletion_index = self.traverse_and_delete(node.left, condition, target_sum, f"{current_path}{node.data}->", current_sum + node.data, deletion_index)
        deletion_index = self.traverse_and_delete(node.right, condition, target_sum, f"{current_path}{node.data}->", current_sum + node.data, deletion_index)

        if node.left is None and node.right is None:
            branch_sum = current_sum + node.data
            if ((condition == "L" and branch_sum < target_sum) or
                (condition == "EQ" and branch_sum == target_sum) or
                (condition == "M" and branch_sum > target_sum)):
                deletion_index += 1
                print(f"{deletion_index}) {current_path}{node.data} = {branch_sum}")
                self.delete_node(node)

        return deletion_index

    def printTree(self, node=None, level=0):
        if node is None:
            node = self.root
            # if level == 0:
            #     print("City A has fallen")
            # return
        if node.right:
            self.printTree(node.right, level + 1)
        print(f" {'     ' * level + str(node.data)}")
        if node.left:
            self.printTree(node.left, level + 1)
            

# Initialize the BST
T = BinarySearchTree()

# Parse input
city, enemy = input("Enter <Create City A (BST)>/<Create conditions and deploy the army>: ").split("/")
city = map(int, city.split())
enemy = [instr.split() for instr in enemy.split(",")]

# Insert nodes into the BST
for data in city:
    T.append(data)

print("(City A) Before the war:")
T.printTree()

# Execute the commands
for op, data in enemy:
    data = int(data)
    print("--------------------------------------------------")
    if op == "L":
        print(f"Removing paths where the sum is less than {data}:")
    elif op == "EQ":
        print(f"Removing paths where the sum is equal to {data}:")
    elif op == "M":
        print(f"Removing paths where the sum is greater than {data}:")

    # Traverse the tree and delete paths based on the conditions
    deletion_index = T.traverse_and_delete(T.root, op, data)
    if deletion_index == 0:
        print("No paths were removed.")
    print("--------------------------------------------------")
    print("(City A) After the war:")
    T.printTree()

'''
testcase 1
Enter <Create City A (BST)>/<Create conditions and deploy the army>: 100 70 200 34 80 300/L 250,EQ 250,M 250
(City A) Before the war:
           300
      200
 100
           80
      70
           34
--------------------------------------------------
Removing paths where the sum is less than 250:
1) 100->70->34 = 204
--------------------------------------------------
(City A) After the war:
           300
      200
 100
           80
      70
--------------------------------------------------
Removing paths where the sum is equal to 250:
1) 100->70->80 = 250
--------------------------------------------------
(City A) After the war:
           300
      200
 100
      70
--------------------------------------------------
Removing paths where the sum is greater than 250:
1) 100->200->300 = 600
2) 100->200 = 300
--------------------------------------------------
(City A) After the war:
 100
      70
    
    
testcase 2
Enter <Create City A (BST)>/<Create conditions and deploy the army>: 1 6 8 7 8 0 2 3 10/L 5,M 5
(City A) Before the war:
                     10
                8
           8
                7
      6
                3
           2
 1
      0
--------------------------------------------------
Removing paths where the sum is less than 5:
1) 1->0 = 1
--------------------------------------------------
(City A) After the war:
                     10
                8
           8
                7
      6
                3
           2
 1
--------------------------------------------------
Removing paths where the sum is greater than 5:
1) 1->6->2->3 = 12
2) 1->6->2 = 9
3) 1->6->8->7 = 22
4) 1->6->8->8->10 = 33
5) 1->6->8->8 = 23
6) 1->6->8 = 15
7) 1->6 = 7
--------------------------------------------------
(City A) After the war:
 1
 
testcase 3
Enter <Create City A (BST)>/<Create conditions and deploy the army>: 555 222 888 777 444 000 555/L 789879
(City A) Before the war:
      888
           777
                555
 555
           444
      222
           0
--------------------------------------------------
Removing paths where the sum is less than 789879:
1) 555->222->0 = 777
2) 555->222->444 = 1221
3) 555->222 = 777
4) 555->888->777->555 = 2775
5) 555->888->777 = 2220
6) 555->888 = 1443
7) 555 = 555
--------------------------------------------------
(City A) After the war:
City A has fallen!


testcase 4
Enter <Create City A (BST)>/<Create conditions and deploy the army>: 0 -1 0 -2 -30 -8 -99 -7 -6/L -40,M -99,EQ 100
(City A) Before the war:
      0
 0
      -1
           -2
                               -6
                          -7
                     -8
                -30
                     -99
--------------------------------------------------
Removing paths where the sum is less than -40:
1) 0->-1->-2->-30->-99 = -132
2) 0->-1->-2->-30->-8->-7->-6 = -54
3) 0->-1->-2->-30->-8->-7 = -48
4) 0->-1->-2->-30->-8 = -41
--------------------------------------------------
(City A) After the war:
      0
 0
      -1
           -2
                -30
--------------------------------------------------
Removing paths where the sum is greater than -99:
1) 0->-1->-2->-30 = -33
2) 0->-1->-2 = -3
3) 0->-1 = -1
4) 0->0 = 0
5) 0 = 0
--------------------------------------------------
(City A) After the war:
City A has fallen!


testcase 5
Enter <Create City A (BST)>/<Create conditions and deploy the army>: 9 8 7 6 7 8 9/L 30,M 30,EQ 30
(City A) Before the war:
      9
 9
           8
      8
                7
           7
                6
--------------------------------------------------
Removing paths where the sum is less than 30:
1) 9->8->8 = 25
2) 9->9 = 18
--------------------------------------------------
(City A) After the war:
 9
      8
                7
           7
                6
--------------------------------------------------
Removing paths where the sum is greater than 30:
1) 9->8->7->7 = 31
--------------------------------------------------
(City A) After the war:
 9
      8
           7
                6
--------------------------------------------------
Removing paths where the sum is equal to 30:
1) 9->8->7->6 = 30
--------------------------------------------------
(City A) After the war:
 9
      8
           7
           
testcase 6
Enter <Create City A (BST)>/<Create conditions and deploy the army>: 1 2 3/EQ 6,EQ 5,EQ 4,EQ 3
(City A) Before the war:
           3
      2
 1
--------------------------------------------------
Removing paths where the sum is equal to 6:
1) 1->2->3 = 6
--------------------------------------------------
(City A) After the war:
      2
 1
--------------------------------------------------
Removing paths where the sum is equal to 5:
No paths were removed.
--------------------------------------------------
(City A) After the war:
      2
 1
--------------------------------------------------
Removing paths where the sum is equal to 4:
No paths were removed.
--------------------------------------------------
(City A) After the war:
      2
 1
--------------------------------------------------
Removing paths where the sum is equal to 3:
1) 1->2 = 3
--------------------------------------------------
(City A) After the war:
 1

test case 7
Enter <Create City A (BST)>/<Create conditions and deploy the army>: 1 1 1 1 1 1 1/M 1,L 1,EQ 1
(City A) Before the war:
                               1
                          1
                     1
                1
           1
      1
 1
--------------------------------------------------
Removing paths where the sum is greater than 1:
1) 1->1->1->1->1->1->1 = 7
2) 1->1->1->1->1->1 = 6
3) 1->1->1->1->1 = 5
4) 1->1->1->1 = 4
5) 1->1->1 = 3
6) 1->1 = 2
--------------------------------------------------
(City A) After the war:
 1
--------------------------------------------------
Removing paths where the sum is less than 1:
No paths were removed.
--------------------------------------------------
(City A) After the war:
 1
--------------------------------------------------
Removing paths where the sum is equal to 1:
1) 1 = 1
--------------------------------------------------
(City A) After the war:
City A has fallen!



'''   

