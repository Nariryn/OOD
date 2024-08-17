'''
พี่ซันฟงได้รับคำสั่งจากอาจารย์ให้ออกโจทย์เขียนโปรแกรมให้แก่น้องๆ พี่จึงกลับไปนอนคิดที่บ้าน รู้สึกตัวอีกทีก็อยู่ในห้องมืดๆ 
พี่สามารถมองเห็นและเดินไปยังพื้นที่ที่อยู่ติดกันได้ (4 ทิศ เหนือ ใต้ ออก ตก) พี่จะต้องหาประตูทางออกจากฝันเพื่อไปส่งโจทย์ให้กับอาจารย์ 
ต่อมาพี่ก็คิดวิธีในการเดินหาประตูทางออกได้โดยใช้วิธีหาแบบ Breadth First Search โดยพี่จะเริ่มยืนในจุดเริ่มต้นแล้วมองหาและจำทางเริ่มจากทิศเหนือ 
ทิศตะวันออก ทิศใต้ ทิศตะวันตก ตามลำดับ แล้วเดินไปยังช่องถัดไปแล้วหาใหม่ 
ในเมื่อคิดวิธีออกแล้วพี่จึงต้องการโปรแกรมที่จะบอกพี่ว่าสามารถไปถึงทางออกได้หรือพี่จะต้องติดอยู่ในฝันไปตลอดกาล ปัญหาคือพี่ขี้เกียจเขียนโค้ด 
พี่เลยอยากให้น้องๆเขียนโค้ดให้พี่หน่อย เขียนสวยๆกะทัดรัด ไม่งั้นจะส่งกลับไปเขียนใหม่
โดยรายละเอียดโปรแกรมจะมีดังนี้
Input
รับความกว้าง ความสูง และแผนที่ โดยแผนที่แต่ละบรรทัดจะขั้นด้วย ','
ตัวอย่าง input: 3 3 F__,##_,O__
จะมีความหมายว่าแผนที่กว้าง 3 สูง 3 และแผนที่จะเป็นแบบนี้
F__
##_
O__
ภายในแผนที่
'F' แทนตำแหน่งเริ่มต้นของพี่
'O' แทนประตูทางออก
'_' แทนพื้นที่ที่สามารถเดินได้
ตัวอักษรอื่นๆทั้งหมดแทนกำแพง ไม่สามารถเดินไปที่ช่องนั้นได้
Output
หากไม่มีพี่ (F) อยู่ในห้องหรือแผนที่ที่ใส่เข้ามาไม่ตรงกับขนาดของ width ให้แสดงว่า "Invalid map input."
แสดง queue ระหว่างหาทางออก
ถ้าหาทางออกเจอให้แสดงว่า "Found the exit portal."
ถ้าหาไม่เจอให้แสดงว่า "Cannot reach the exit portal."

1.Enter width, height, and room: 6 4 F__###,##_###,##__##,###__O
Queue: [(0, 0)]
Queue: [(1, 0)]
Queue: [(2, 0)]
Queue: [(2, 1)]
Queue: [(2, 2)]
Queue: [(3, 2)]
Queue: [(3, 3)]
Queue: [(4, 3)]
Found the exit portal.

2.Enter width, height, and room: 8 6 ########,##___###,##_F_###,##____##,##_##_O_,##______
Queue: [(3, 2)]
Queue: [(3, 1), (4, 2), (3, 3), (2, 2)]
Queue: [(4, 2), (3, 3), (2, 2), (4, 1), (2, 1)]
Queue: [(3, 3), (2, 2), (4, 1), (2, 1), (4, 3)]
Queue: [(2, 2), (4, 1), (2, 1), (4, 3), (2, 3)]
Queue: [(4, 1), (2, 1), (4, 3), (2, 3)]
Queue: [(2, 1), (4, 3), (2, 3)]
Queue: [(4, 3), (2, 3)]
Queue: [(2, 3), (5, 3)]
Queue: [(5, 3), (2, 4)]
Queue: [(2, 4), (5, 4)]
Queue: [(5, 4), (2, 5)]
Found the exit portal.

3.Enter width, height, and room: 3 3 ###,######F,###
Invalid map input.

4.Enter width, height, and room: 3 3 F__,##_,O_
Invalid map input.

5.Enter width, height, and room: 1 1 F
Queue: [(0, 0)]
Cannot reach the exit portal.

6.Enter width, height, and room: 2 1 FO
Queue: [(0, 0)]
Found the exit portal.

7.Enter width, height, and room: 5 3 __|__,F_|_O,__|__
Queue: [(0, 1)]
Queue: [(0, 0), (1, 1), (0, 2)]
Queue: [(1, 1), (0, 2), (1, 0)]
Queue: [(0, 2), (1, 0), (1, 2)]
Queue: [(1, 0), (1, 2)]
Queue: [(1, 2)]
Cannot reach the exit portal.

8.Enter width, height, and room: 10 7 F_____\...,===\___\..,...#\___\.,....#|___|,...#/___/.,===/___/..,O_____/...
Queue: [(0, 0)]
Queue: [(1, 0)]
Queue: [(2, 0)]
Queue: [(3, 0)]
Queue: [(4, 0)]
Queue: [(5, 0), (4, 1)]
Queue: [(4, 1), (5, 1)]
Queue: [(5, 1)]
Queue: [(6, 1), (5, 2)]
Queue: [(5, 2), (6, 2)]
Queue: [(6, 2)]
Queue: [(7, 2), (6, 3)]
Queue: [(6, 3), (7, 3)]
Queue: [(7, 3), (6, 4)]
Queue: [(6, 4), (8, 3), (7, 4)]
Queue: [(8, 3), (7, 4), (6, 5), (5, 4)]
Queue: [(7, 4), (6, 5), (5, 4)]
Queue: [(6, 5), (5, 4)]
Queue: [(5, 4), (5, 5)]
Queue: [(5, 5)]
Queue: [(5, 6), (4, 5)]
Queue: [(4, 5), (4, 6)]
Queue: [(4, 6)]
Queue: [(3, 6)]
Queue: [(2, 6)]
Queue: [(1, 6)]
Found the exit portal.

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
    
    def __str__(self) -> str:
        return str(self.items)

width,height,room = input('Enter width, height, and room: ').split()
data = room.split(",")
final = []
went = []
queue = Queue()
found_f = False
for row in data:
    preroom = []
    for column in row:
        preroom.append(column)
        if column == 'F':
            went.append((row.index(column),data.index(row)))
            queue.enqueue((row.index(column),data.index(row)))
            found_f = True
    if len(preroom) != int(width):
        print('Invalid map input.')
        exit()
    final.append(preroom)
if len(final) != int(height):
    print('Invalid map input.')
    exit()
if not found_f:
    print('Invalid map input.')
    exit()

scan_set = [(0,-1),(1,0),(0,1),(-1,0)]
while not queue.is_empty():
    print('Queue:',queue)
    x,y = queue.dequeue()
    for setx,sety in scan_set:
        if y+sety >= 0 and y+sety < int(height) and x+setx >= 0 and x+setx < int(width):
            pos = final[y+sety][x+setx]
            if pos == 'O':
                print('Found the exit portal.')
                exit()
            elif pos == '_' and (x+setx,y+sety) not in went :
                went.append((x+setx,y+sety))
                queue.enqueue((x+setx,y+sety))
print('Cannot reach the exit portal.')