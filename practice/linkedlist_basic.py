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

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def  __init__(self):
        self.head = Node(None)
        
    def __str__(self) -> str:
        result = []
        current = self.head.next
        while current:
            result.append(str(current.data))
            current = current.next
        if result:
            return '->'.join(result)
        else:
            return 'Empty list'
    
    def append(self, data):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
    
    def is_empty(self):
        return self.head == None
    
    def insert(self, index, data):
        if index < 0:
            print ("Data cannot be added")
            return
        
        current = self.head
        pos = 0

        while current and pos < index:
            current = current.next
            pos += 1
        
        if not current:
            print("Data cannot be added")
            return
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        
    def print_list(self):
        print(self)
        
def process_input(input_str):
    parts = input_str.split(",")
    num_data = parts[0]
    operation = parts[1:]
    
    L = LinkedList()
    
    if num_data:
        for item in num_data.split():
            L.append(int(item))
            
    print(f"link list : {L}")
    
    for i in operation:
        if ":" in i:
            index, data = map(int, i.split(":"))
            print(f"index = {index} and data = {data}")
            L.insert(index, data)
            print(f"link list : {L}")
            
inp = input("Enter Input : ")
process_input(inp)
    