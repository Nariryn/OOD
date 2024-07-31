class Stack:
    def __init__(self, ls = None) -> None:
        if ls is None:
            self.items = []
        else:
            self.items = ls
        self.size = 0
        self.top = 0
            
    def push(self, data):
        self.items.append(data)
        self.size += 1
        self.top += 1
        
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            self.items.pop()
        self.size -=1
        self.top -=1
        
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
inp_str = input("Enter Input : ").split(",")
s = Stack()

for cmd in inp_str:
    if cmd[0] == "A":
        cmd_type, value = cmd.split()
        s.push(value)
        print(f"Add = {value} and Size = {s.size}")
    elif cmd[0] == "P":
        if s.size >= 1:
            value = s.peek()
            s.pop()
            print(f"Pop = {value} and Index = {s.size}")
            continue
        print(-1)
        continue

s_str  = ' '.join(s.items)

if s.is_empty():
    print("Value in Stack = Empty")
else:
    print(f"Value in Stack = {s_str}")
    
    
'''
Chapter : 3 - item : 1 - รู้จักกับ STACK

ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา


A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

P                 ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

*** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

Test Case #1
Enter Input : A 10,A 20,A 30,A 40,P,P
Add = 10 and Size = 1
Add = 20 and Size = 2
Add = 30 and Size = 3
Add = 40 and Size = 4
Pop = 40 and Index = 3
Pop = 30 and Index = 2
Value in Stack = 10 20

Test Case #2
Enter Input : A 10,A 20,A 30,A 40,P,A 50,A 60,P,P,P,P,P,P
Add = 10 and Size = 1
Add = 20 and Size = 2
Add = 30 and Size = 3
Add = 40 and Size = 4
Pop = 40 and Index = 3
Add = 50 and Size = 4
Add = 60 and Size = 5
Pop = 60 and Index = 4
Pop = 50 and Index = 3
Pop = 30 and Index = 2
Pop = 20 and Index = 1
Pop = 10 and Index = 0
-1
Value in Stack = Empty

Test Case #4
Enter Input : P,A 99,P,P,A 88,P,P,A 12,A 13,A 86
-1
Add = 99 and Size = 1
Pop = 99 and Index = 0
-1
Add = 88 and Size = 1
Pop = 88 and Index = 0
-1
Add = 12 and Size = 1
Add = 13 and Size = 2
Add = 86 and Size = 3
Value in Stack = 12 13 86



'''