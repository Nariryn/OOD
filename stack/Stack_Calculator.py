'''
ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
+: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
-: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
*: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
/: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
DUP: Duplicate (not double) ค่าบนสุดของ stack
POP: Pop ค่าบนสุดออกจาก stack และ discard.
PSH: ทำการ push ตัวเลขลง stack
หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
*************************************************
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())

1. * Stack Calculator *
    Enter arguments : 5 6 +
    11
2. * Stack Calculator *
    Enter arguments : 3 DUP +
    6
3. * Stack Calculator *
    Enter arguments : 6 5 5 7 * - /
    5
4. * Stack Calculator *
    Enter arguments : a b c +
    Invalid instruction: a
5. * Stack Calculator *
    Enter arguments : 12
    12
6. * Stack Calculator *
    Enter arguments : 9 14 DUP + - 3 POP
    19
7. * Stack Calculator *
    Enter arguments : 1 2 3 4 5 POP POP POP
    2
8. * Stack Calculator *
    Enter arguments : 13 DUP 4 POP 5 DUP + DUP + -
    7
9. * Stack Calculator *
    Enter arguments : 4 POP
    0
'''
class Stack:
    def __init__(self):
        self.ls=[]
    def push(self,new):
        self.ls.append(new)
    def pop(self):
        out = self.ls.pop()
        return out
    def isEmpty(self):
        if(len(self.ls)==0):
            return True
        else:
            return False
    def size(self):
        return len(self.ls)

def StackCalculator(data):
    stack = Stack()
    for func in data:
        if (func=='+'):
            x = stack.pop()
            y = stack.pop()
            stack.push(x+y)
        elif(func=='-'):
            x = stack.pop()
            y = stack.pop()
            stack.push(x-y)
        elif(func=='*'):
            x = stack.pop()
            y = stack.pop()
            stack.push(x*y)
        elif(func=='/'):
            x = stack.pop()
            y = stack.pop()
            stack.push(x//y)
        elif(func=='POP'):
            stack.pop()
        elif(func=='DUP'):
            x = stack.pop()
            stack.push(x)
            stack.push(x)
        elif(func=='PSH'):
            stack.push()
        elif(func.isalpha()):
            return 'Invalid instruction: '+func
        else:
            stack.push(int(func))
    if stack.isEmpty() == False:
        return int(stack.pop())
    else:
        return 0

class StackCalc:
    def __init__(self):
        self.ans = 0
    def run(self,arg):
        data = arg.split()
        self.ans = StackCalculator(data)
    def getValue(self):
        return self.ans
    
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())