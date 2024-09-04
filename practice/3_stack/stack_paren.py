class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, data):
        self.items.append(data)
        
    def __len__(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
        
    def pop(self):
        if len(self) == 0:
            return "Empty"
        else:
            return self.items.pop()
    
    
    def __str__(self) -> str:
        return ''.join(self.items)
    

x = input("Enter expresion : ")
Open = Stack()
for char in x:
    if char in "([{":
        Open.push(char)
    if char in "}])" and len(Open) == 0:
        print(x,"close paren excess")
        exit()
    elif char in "}])":
        if char == "]":
            if Open.peek() == "[":
                Open.pop()
            else:
                print(x,"Unmatch open-close")
                exit()
        if char == ")":
            if Open.peek() == "(":
                Open.pop()
            else:
                print(x,"Unmatch open-close")
                exit()
        if char == "}":
            if Open.peek() == "{":
                Open.pop()
            else:
                print(x,"Unmatch open-close")
                exit()
if len(Open) == 0:
    print(x,"MATCH")
else:
    print(x,"open paren excess  ",len(Open),":",Open)
    
'''

จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา

โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด

1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด

2. วงเล็บปิดเกิน

3. วงเล็บเปิดเกิน

แล้วให้แสดงผลตามตัวอย่าง



testcase 1
Enter expresion : [[)))))
[[))))) Unmatch open-close  

testcase 2
Enter expresion : [[))
[[)) Unmatch open-close  

testcase 3
Enter expresion : (())))
(()))) close paren excess

testcase 4
Enter expresion : )}]
)}] close paren excess

testcase 5
Enter expresion : (((
((( open paren excess   3 : (((


testcase 6
Enter expresion : (a+c)(a-b)*c(-a
(a+c)(a-b)*c(-a open paren excess   1 : (
  
testcsae 7
Enter expresion : (([]))
(([])) MATCH

testcase 8
Enter expresion : (){}[]}
(){}[]} close paren excess

'''