'''
กฤษฎาได้มาทำงานพิเศษในช่วงปิดเทอมที่ร้านหนังสือการ์ตูนแห่งหนึ่ง  โดยเจ้าของร้านได้สั่งให้กฤษฎามาจัดหนังสือการ์ตูน Attack On Titan เพื่อที่จะวางขายในวันรุ่งขึ้น  โดยกฤษฎาได้จัดหนังสือไปเรื่อยๆจนรู้สึกเบื่อหน่าย  จึงได้คิดเกมสนุกๆขึ้นมานั่นคือ  ในชั้นหนังสือจะมีแค่ด้านหน้ากับด้านหลังที่จะใส่หนังสือเข้าไปได้เรื่อยๆ และจะนำหนังสือออกได้แค่ด้านหน้า และใส่หนังสือเพิ่มได้แค่ด้านหลัง  โดยเมื่อเล่นเกมนี้ไปเรื่อยๆ กฤษฎาก็ลืมว่าในชั้นหนังสือนั้นมีหนังสือซ้ำกันหรือไม่  กฤษฎาเลยอยากให้คุณเขียนโปรแกรม Python เพื่อมาช่วยกฤษฎาคิดว่ามีหนังสือซ้ำกันในชั้นนั้นหรือไม่

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นหนังสือที่มีอยู่ในชั้นอยู่แล้ว  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
D                -> เป้นการนำหนังสือด้านหน้าออกจากชั้น
E <value>   -> เป็นการนำหนังสือ Attack On Titan เล่มที่ value เข้าชั้นหนังสือจากด้านหลัง


Testcase student: #1
Enter Input : 1 2 7 2 4 6 8/E 5,D,D,E 1,E 3,D
NO Duplicate

Testcase student: #2
Enter Input : 1 1 1 1/E 2,E 3,D,D
Duplicate
'''

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
    
inp = input("Enter Input : ").split("/")
book = inp[0].split(" ")
cmds  = inp[1].split(",")

book_shelf = Queue(book)

for cmd in cmds:
    if cmd[0] == "E":
        cmd_type, value = cmd.split(" ")
        book_shelf.enqueue(value)
    elif cmd[0] == "D":
        book_shelf.dequeue()
        
book_seen = set()
found_dup = False

for book in book_shelf.items:
    if book in book_seen:
        found_dup = True
        break
    book_seen.add(book)
    
if found_dup == True:
    print ("Duplicate")
else:
    print ("No Duplicate")