class Stack():
    
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
        return None if self.isEmpty() else self.stack[-1]
    
    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False
        
    def size (self):
        return len(self.stack)

class StackCalc:
    def __init__(self):
        self.stack = Stack()
        self.error = None
        
    def run(self, inp):
        for inp in inp.split():
            if inp.lstrip("-").isdigit():
                self.stack.push(int(inp))
            elif inp == "+":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(a + b)
            elif inp == "-":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(a - b)
            elif inp == "*":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(a * b)
            elif inp == "/":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(a // b)
            elif inp == "DUP":
                self.stack.push(self.stack.peek())
            elif inp == "POP":
                self.stack.pop()
            else:
                self.error = f"Invalid instruction: {inp}"
                return
            
    def getValue(self):
        if self.error:
            return self.error
        elif not self.stack.isEmpty():
            return self.stack.peek()
        else:
            return 0

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())