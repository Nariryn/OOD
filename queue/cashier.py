'''
จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2]

1.Enter people and time : HELLO_WORLD 13
1 ['E', 'L', 'L', 'O', '_', 'W', 'O', 'R', 'L', 'D'] ['H'] []
2 ['L', 'L', 'O', '_', 'W', 'O', 'R', 'L', 'D'] ['H', 'E'] []
3 ['L', 'O', '_', 'W', 'O', 'R', 'L', 'D'] ['H', 'E', 'L'] []
4 ['O', '_', 'W', 'O', 'R', 'L', 'D'] ['E', 'L', 'L'] []
5 ['_', 'W', 'O', 'R', 'L', 'D'] ['E', 'L', 'L', 'O'] []
6 ['W', 'O', 'R', 'L', 'D'] ['E', 'L', 'L', 'O', '_'] []
7 ['O', 'R', 'L', 'D'] ['L', 'L', 'O', '_', 'W'] []
8 ['R', 'L', 'D'] ['L', 'L', 'O', '_', 'W'] ['O']
9 ['L', 'D'] ['L', 'L', 'O', '_', 'W'] ['O', 'R']
10 ['D'] ['L', 'O', '_', 'W', 'L'] ['R']
11 [] ['L', 'O', '_', 'W', 'L'] ['R', 'D']
12 [] ['L', 'O', '_', 'W', 'L'] ['D']
13 [] ['O', '_', 'W', 'L'] ['D']

2.Enter people and time : QUEUE_IS_EASY 7
1 ['U', 'E', 'U', 'E', '_', 'I', 'S', '_', 'E', 'A', 'S', 'Y'] ['Q'] []
2 ['E', 'U', 'E', '_', 'I', 'S', '_', 'E', 'A', 'S', 'Y'] ['Q', 'U'] []
3 ['U', 'E', '_', 'I', 'S', '_', 'E', 'A', 'S', 'Y'] ['Q', 'U', 'E'] []
4 ['E', '_', 'I', 'S', '_', 'E', 'A', 'S', 'Y'] ['U', 'E', 'U'] []
5 ['_', 'I', 'S', '_', 'E', 'A', 'S', 'Y'] ['U', 'E', 'U', 'E'] []
6 ['I', 'S', '_', 'E', 'A', 'S', 'Y'] ['U', 'E', 'U', 'E', '_'] []
7 ['S', '_', 'E', 'A', 'S', 'Y'] ['E', 'U', 'E', '_', 'I'] []

3.Enter people and time : IT_OVER_900000000! 20
1 ['T', '_', 'O', 'V', 'E', 'R', '_', '9', '0', '0', '0', '0', '0', '0', '0', '0', '!'] ['I'] []
2 ['_', 'O', 'V', 'E', 'R', '_', '9', '0', '0', '0', '0', '0', '0', '0', '0', '!'] ['I', 'T'] []
3 ['O', 'V', 'E', 'R', '_', '9', '0', '0', '0', '0', '0', '0', '0', '0', '!'] ['I', 'T', '_'] []
4 ['V', 'E', 'R', '_', '9', '0', '0', '0', '0', '0', '0', '0', '0', '!'] ['T', '_', 'O'] []
5 ['E', 'R', '_', '9', '0', '0', '0', '0', '0', '0', '0', '0', '!'] ['T', '_', 'O', 'V'] []
6 ['R', '_', '9', '0', '0', '0', '0', '0', '0', '0', '0', '!'] ['T', '_', 'O', 'V', 'E'] []
7 ['_', '9', '0', '0', '0', '0', '0', '0', '0', '0', '!'] ['_', 'O', 'V', 'E', 'R'] []
8 ['9', '0', '0', '0', '0', '0', '0', '0', '0', '!'] ['_', 'O', 'V', 'E', 'R'] ['_']
9 ['0', '0', '0', '0', '0', '0', '0', '0', '!'] ['_', 'O', 'V', 'E', 'R'] ['_', '9']
10 ['0', '0', '0', '0', '0', '0', '0', '!'] ['O', 'V', 'E', 'R', '0'] ['9']
11 ['0', '0', '0', '0', '0', '0', '!'] ['O', 'V', 'E', 'R', '0'] ['9', '0']
12 ['0', '0', '0', '0', '0', '!'] ['O', 'V', 'E', 'R', '0'] ['0', '0']
13 ['0', '0', '0', '0', '!'] ['V', 'E', 'R', '0', '0'] ['0', '0']
14 ['0', '0', '0', '!'] ['V', 'E', 'R', '0', '0'] ['0', '0']
15 ['0', '0', '!'] ['V', 'E', 'R', '0', '0'] ['0', '0', '0']
16 ['0', '!'] ['E', 'R', '0', '0', '0'] ['0', '0']
17 ['!'] ['E', 'R', '0', '0', '0'] ['0', '0', '0']
18 [] ['E', 'R', '0', '0', '0'] ['0', '0', '!']
19 [] ['R', '0', '0', '0'] ['0', '0', '!']
20 [] ['R', '0', '0', '0'] ['0', '!']

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
    
    def getItem(self):
        output = self.items
        return output

firstqueue = Queue()
secondqueue = Queue()
lastqueue = Queue()
time1 = 0
time2 = 0
data,time = input('Enter people and time : ').split()
for i in data:
    firstqueue.enqueue(i)
for i in range(1,int(time)+1):
    if time1 == 3 and not secondqueue.is_empty():
        secondqueue.dequeue()
        time1 = 0
    if time2%2 == 0  and not lastqueue.is_empty():
        lastqueue.dequeue()
    if len(secondqueue.getItem())<5 and not firstqueue.is_empty():
        secondqueue.enqueue(firstqueue.dequeue())
    else:
        if not firstqueue.is_empty():
            lastqueue.enqueue(firstqueue.dequeue())
    time1+=1
    if not lastqueue.is_empty():
        time2+=1
    print(f'{i} {firstqueue.getItem()} {secondqueue.getItem()} {lastqueue.getItem()}')

    
