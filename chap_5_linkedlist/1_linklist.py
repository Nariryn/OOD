class Node:
    def __init__(self,data, next):
        self.data = data
        self.next = next
    
    def __str__(self) -> str:
        return f"{self.data}"

class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.length = 0

    def __str__(self) -> str:
        current, str = self.head, []
        while current.next is not None:
            str.append(current.next.data)
            current = current.next
        str = '->'.join(str)
        return str

    def __len__ (self):
        return self.length

    def is_empty(self):
        return self.head.next is None
    
    def append(self, data):
        node = Node(str(data), None)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        self.length += 1
    
    def insert(self, index, data):
        if index == self.length:
            self.append(data)
            return
        node = Node(str(data), None)
        index_inp = 0
        current = self.head

        while current.next is not None:
            if index_inp == index:
                node.next = current.next
                current.next = node
                break
            current = current.next
            index_inp += 1

        self.length += 1

class Solve(LinkedList):
    def __init__(self, input:str):
        super().__init__()
        self.initial = input

    def solve(self):
        inp = self.initial[0]
        if inp == "":
            print("List is empty")
        else:
            inp = inp.split()
            for i in inp:
                self.append(i)
            print(f"link list : {self}")
        for i in range(1, len(self.initial)):
            element = self.initial[i].strip()
            element = element.split(":")
            if int(element[0]) < 0 or int(element[0]) > len(self):
                print ("Data cannot be added")
            else:
                print(f"index = {element[0]} and data = {element[1]}")
                self.insert(int(element[0]), element[1])
            if self.is_empty():
                print("List is empty")
            else:
                print(f"link list : {self}")
                

            

inp = input("Enter Input : ").split(",")
solver = Solve(inp)
solver.solve()


'''
สร้าง method insert ในคลาส LinkedList เพื่อแทรกข้อมูลลงใน index ที่กำหนดของ linked list และ return ผลลัพธ์ตามตัวอย่าง 

โดยคลาส LinkedList จะประกอบไปด้วย

1. def __init__(self): สำหรับสร้าง linked list

2. def __str__(self): return string แสดง ค่าใน linked list

3. def isEmpty(self): return list นั้นว่างหรือไม่

4. def append(self, data): เพิ่ม data ต่อท้าย linked list

5. def insert(self, index, data): insert data ใน index ที่กำหนด

โดยการแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Header Node ดูนะครับ

*******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********

class Node:
    def __init__(self, data):
        self.data = data
     


ข้อมูลอินพุท จะคั่นด้วยเครื่องหมาย คอมม่า

ตัวแรก จะเป็น ลิสต์ตั้งต้น คั่นด้วยช่องว่าง (space)

ตัวต่อไปจะอยู่ในรูปแบบ index:data

Enter Input : 1 2 3 4, 0:7, 3:9
ลิสต์ตั้งต้นคือ 1->2->3-> 4

ข้อมูล 0:0 คือให้เพิ่ม node ลำดับ 0 โดยมีข้อมูลเป็น 7

ข้อมูล 3:9 คือให้เพิ่ม node ลำดับ 3 โดยมีข้อมูลเป็น 9

test case 1
Enter Input : 1 2, 0:0, 3:3
link list : 1->2
index = 0 and data = 0
link list : 0->1->2
index = 3 and data = 3
link list : 0->1->2->3

test case 2
Enter Input : 0 1 2, -1:3, 10:10
link list : 0->1->2
Data cannot be added
link list : 0->1->2
Data cannot be added
link list : 0->1->2

test case 3
Enter Input : 0 1 2 4, 3:3
link list : 0->1->2->4
index = 3 and data = 3
link list : 0->1->2->3->4

test case 4
Enter Input : ,0:0,1:1
List is empty
index = 0 and data = 0
link list : 0
index = 1 and data = 1
link list : 0->1

test case 5
Enter Input : ,1:1
List is empty
Data cannot be added
List is empty

test case 6
Enter Input : 0 1 2 4, -1:2, 3:3, 5:5, 0:-1
link list : 0->1->2->4
Data cannot be added
link list : 0->1->2->4
index = 3 and data = 3
link list : 0->1->2->3->4
index = 5 and data = 5
link list : 0->1->2->3->4->5
index = 0 and data = -1
link list : -1->0->1->2->3->4->5


'''