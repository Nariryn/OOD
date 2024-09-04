class Queue:
    def __init__(self, ls = None):
        if ls is None:
            self.items = []
        else:
            self.items = ls
            
    def enqueue (self, data):
        self.items.append(data)
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)
        
    def is_empty(self):
        return len(self.items) == 0

    def __len__ (self):
        return len(self.items)
    
inp = input("Enter Input : ").split(",")

q = Queue()
q_remove = []
for cmd in inp:
    if cmd[0] == "E":
        cmd_type, value = cmd.split(" ")
        q.enqueue(value)
        print(f"Add {value} index is {len(q.items)-1}")
    elif cmd[0] == "D":
        if len(q) >= 1:
            value = q.dequeue()
            q_remove.append(value)
            print(f"Pop {value} size in queue is {len(q.items)}")
            continue
        print(-1)
        continue
            
if q.is_empty():
    print ("Empty")
else:
    print (f"Number in Queue is :  {q.items}")
    
'''
item : 1 - Basic Queue
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา

E valueให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป

D ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queue หลังจากทำการ dequeue แล้ว

*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา ถ้าหากไม่มีแล้วให้แสดงคำว่า Empty ***

Test Case #1
Enter Input : E 10,E 20,E 30,E 40,D,D
Add 10 index is 0
Add 20 index is 1
Add 30 index is 2
Add 40 index is 3
Pop 10 size in queue is 3
Pop 20 size in queue is 2
Number in Queue is :  ['30', '40']

Test Case #2
Enter Input : E 10,E 20,E 30,E 40,D,E 50,E 60,D,D,D,D,D,D
Add 10 index is 0
Add 20 index is 1
Add 30 index is 2
Add 40 index is 3
Pop 10 size in queue is 3
Add 50 index is 3
Add 60 index is 4
Pop 20 size in queue is 4
Pop 30 size in queue is 3
Pop 40 size in queue is 2
Pop 50 size in queue is 1
Pop 60 size in queue is 0
-1
Empty

Test Case #3
Enter Input : D,D,D,D,D
-1
-1
-1
-1
-1
Empty

Test Case #4
Enter Input : D,E 99,D,D,E 88,D,D,E 12,E 13,E 86
-1
Add 99 index is 0
Pop 99 size in queue is 0
-1
Add 88 index is 0
Pop 88 size in queue is 0
-1
Add 12 index is 0
Add 13 index is 1
Add 86 index is 2
Number in Queue is :  ['12', '13', '86']

'''