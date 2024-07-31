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


'''
ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
+: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
-: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
*: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
/: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
DUP: Duplicate (not double) ค่าบนสุดของ stack
POP: Pop ค่าบนสุดออกจาก stack และ discard.
PSH: ทำการ push ตัวเลขลง stack
หมายเหตุ 1. คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
2. การนำค่าออกจาก stack สำหรับ calculator นี้ให้ การนำค่าออกจาก stack ครั้งแรกเป็น operand ด้านซ้าย และ การนำค่าออกจาก stack ครั้งที่ 2 เป็น operand ด้านขวา
*************************************************
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())


testcase 1
* Stack Calculator *
Enter arguments : 5 6 +
11

testcase 2
* Stack Calculator *
Enter arguments : 3 DUP +
6

testcase 3
* Stack Calculator *
Enter arguments : 6 5 5 7 * - /
5

testcase 4
* Stack Calculator *
Enter arguments : a b c +
Invalid instruction: a

testcase 5
* Stack Calculator *
Enter arguments : 12
12

testcase 6
* Stack Calculator *
Enter arguments : 9 14 DUP + - 3 POP
19

testcase 7
* Stack Calculator *
Enter arguments : 1 2 3 4 5 POP POP POP
2

testcase 8
* Stack Calculator *
Enter arguments : 4 POP
0


'''