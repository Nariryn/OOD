'''
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา

E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผล Size ปัจจุบันของ QUEUE

D  ให้ทำการแสดงผลของvalueที่อยู่หน้าสุดและindexของvalueนั้นจากนั้นทำการ De_QUEUE ถ้าหากไม่มี value อยู่ใน Queue ให้แสดงผลเป็น  -1

*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

1.Enter Input : E 10,E 20,E 30,E 40,D,D
1
2
3
4
10 0
20 0
30 40

2.Enter Input : E 10,E 20,E 30,E 40,D,E 50,E 60,D,D,D,D,D,D
1
2
3
4
10 0
4
5
20 0
30 0
40 0
50 0
60 0
-1
Empty
'''
class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        if len(self.items)>0:
            return self.items.pop(0)
    def leng(self):
        return len(self.items)
    
    def __str__(self):
        output = ""
        if not self.is_empty():
            for item in self.items:
                output += str(item) + ' '
        else:
            output = 'Empty'
        return output
    

queue = Queue()
data = input('Enter Input : ').split(',')
for i in data:
    if len(i) == 1:
        if not queue.is_empty():
            print(queue.dequeue(), 0)
        else:
            print(-1)
    else:
        value = i.split()[1]
        queue.enqueue(value)
        print(queue.leng())
print(queue)