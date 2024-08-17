'''
โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน 
ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
E < id >  ->   เป็นการนำพนักงานเข้า Queue
D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty

อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 และแผนก 2 id=201,202  
ต่อมาจะแสดงผล Empty เพราะยังไม่มีพนักงานในแถว  และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ 
ต่อมาจะแสดงผลเป็น 101 เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก

1.Enter Input : 1 101,1 102,2 201,2 202/D,E 101,E 201,D,D
Empty
101
201

2.Enter Input : 1 101,1 102,2 201,2 202/D,E 101,E 201,E 102,D,D,D,D
Empty
101
102
201
Empty

3.Enter Input : 1 41,1 42,1 43,2 201,2 202,2 203/E 41,E 201,D,E 202,E 42,E 43,D,E 203,D,D,D
41
201
202
203
42

4.Enter Input : 1 41,1 42,1 43,2 201,2 202,2 203,3 301,3 302,3 303/D,E 41,E 201,E 42,D,D,E 43,E 303,E 41,E 202,E 302,D,D,D,D,D,D,D
Empty
41
42
201
202
43
41
303
302
Empty

5.Enter Input : 1 41,1 42,1 43,2 201,2 202,2 203,3 301,3 302,3 303/D,E 41,E 201,E 42,D,D,E 43,E 303,E 41,E 202,E 302,D,D,D,D,D,D,D,E 301,E 302,E 43,E 42,E 201,E 202,D,E 303,D,D,D,D,D,E 303,D,D,D
Empty
41
42
201
202
43
41
303
302
Empty
301
302
303
43
42
201
202
303
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
    
    def getItem(self):
        output = self.items
        return output
       
    def size(self):
        return len(self.items)
           
    def __str__(self) -> str:
        return str(self.items)

ip = input('Enter Input : ').split('/')
data = ip[0].split(',')
cms = ip[1].split(',')

listdata = {}
for person in data:
    part,person_id = person.split()
    if part not in listdata:
        listdata[part] = []
    listdata[part].append(person_id)

listcm = {}
for cm in cms:
    if cm == 'D':
        is_found = False
        newlistcm = listcm.copy()
        for c in newlistcm:
            if listcm[c].size() == 0:
                continue
            else:
                print(listcm[c].dequeue())
                is_found = True
                break
        for c in newlistcm:
            if listcm[c].size() == 0:
                del listcm[c]
        if not is_found:
            print('Empty')
    else:
        addid = cm.split()[1]
        for c in listdata:
            if addid in listdata[c]:
                if c not in listcm:
                    listcm[c] = Queue()
                listcm[c].enqueue(addid)

