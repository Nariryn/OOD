class Stack ():
    def __init__(self, ls = None):
        if ls is None:
            self.stack = []
        else:
            self.stack = ls
            
    def push(self, i):
        self.stack.append(i)    
            
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return None if self.isempty() else self.stack[-1]
            
    def isempty(self):
        if self.stack == []:
            return  True
        else:
            return False
        
    def size(self):
        return len(self.stack)
    
    
def forest(lst):
    trees = Stack()
    for i in lst:
        cmd = i.split(" ")
        if cmd[0] == "A":
            trees.push(int(cmd[1]))
        elif cmd[0] == "B":
            #look back
            count = 0
            max_height = -1
            for h in reversed(trees.stack):
                if h > max_height:
                    count += 1
                    max_height = h
            print(count)
        elif cmd[0] == "S":
            #effect of  mushroom
            toxic_trees = []
            for h in trees.stack:
                if h % 2 == 0:
                    toxic_height = max(1, h - 1)
                else:
                    toxic_height = h + 2
                toxic_trees.append(toxic_height)
            trees.stack = toxic_trees

inp = [e for e in input("Enter Input : ").split(",")]
forest(inp)