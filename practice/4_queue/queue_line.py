class Queue:
    def __init__(self, ls = None ):
        if ls is None:
            self.items = []
        else:
            self.items = ls
            
    def enqueue(self, data):
        self.items.append(data)
        
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)
        
    def is_empty(self):
        return len(self.items) == 0
    
    def __len__(self):
        return len(self.items)
    
    def get_item(self):
        output = self.items
        return output
    
first_queue = Queue()
secound_queue = Queue()
last_queue = Queue()
time_1 = 0
time_2 = 0

data, time = input("Enter people and time : ").split()

for i in data:
    first_queue.enqueue(i)
    
for i in range(1, int(time)+1):
    if time_1 == 3 and not secound_queue.is_empty():
        secound_queue.dequeue()
        time_1 = 0
    if time_2 % 2 == 0 and not last_queue.is_empty():
        last_queue.dequeue()
    if len(secound_queue.get_item()) < 5 and not first_queue.is_empty():
        secound_queue.enqueue(first_queue.dequeue())
    else:
        if not first_queue.is_empty():
            last_queue.enqueue(first_queue.dequeue())
    time_1 += 1
    if not last_queue.is_empty():
        time_2 += 1
        
    print (f"{i} {first_queue.get_item()} {secound_queue.get_item()} {last_queue.get_item()}")
    

'''
item : 2 - แถวคอย
จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ
แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ
ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2
จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2]

Test Case #1
Enter people and time : HELLO_WORLD 13
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

Test Case #2
Enter people and time : QUEUE_IS_EASY 7
1 ['U', 'E', 'U', 'E', '_', 'I', 'S', '_', 'E', 'A', 'S', 'Y'] ['Q'] []
2 ['E', 'U', 'E', '_', 'I', 'S', '_', 'E', 'A', 'S', 'Y'] ['Q', 'U'] []
3 ['U', 'E', '_', 'I', 'S', '_', 'E', 'A', 'S', 'Y'] ['Q', 'U', 'E'] []
4 ['E', '_', 'I', 'S', '_', 'E', 'A', 'S', 'Y'] ['U', 'E', 'U'] []
5 ['_', 'I', 'S', '_', 'E', 'A', 'S', 'Y'] ['U', 'E', 'U', 'E'] []
6 ['I', 'S', '_', 'E', 'A', 'S', 'Y'] ['U', 'E', 'U', 'E', '_'] []
7 ['S', '_', 'E', 'A', 'S', 'Y'] ['E', 'U', 'E', '_', 'I'] []

Test Case #3
Enter people and time : IT_OVER_900000000! 20
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
    
