class Stack:
    def __init__(self, ls = None) -> None:
        if ls is None:
            self.items =  []
        else:
            self.items = ls
        self.size = 0
    
    def push(self, data):
        self.items.append(data)
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            self.items.pop()
            self.size -= 1
            
        
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
inp = input("Enter Input : ").split(",")

weights = []
frequencies = []
for command in inp:
    weight, frequency = (int(n) for n in command.split(' '))
    while (weights and frequencies) and (weights[-1] < weight):
        print(frequencies.pop())
        weights.pop()
    weights.append(weight)
    frequencies.append(frequency)
    continue


'''
Chapter : 3 - item : 2 - แ ต ก ดั ง เ พ ล้ ง ! ! !

กฤษฎาได้ถูกคุณแม่ไหว้วานให้ล้างจานกองเป็นภูเขา  แต่ทว่ากฤษฎาก็ได้สังเกตเห็นว่าจานแต่ละใบนั้นมีน้ำหนักที่แตกต่างกัน และบนจานยังมีตัวเลขอีกด้วย  กฤษฎาได้เหม่อลอยเนื่องจากครุ่นคริสว่าตัวเลขนั้นหมายถึงอะไร  กฤษฎาก็ได้ทำจานหลุดมือจนจานแตก  และเมื่อจานแตกได้มีเสียงที่มีความถี่ตามเลขบนจาน  กฤษฎาจึงนึกสนุกได้นำจานขนาดต่างๆและมีความถี่ต่างกันมาวางซ้อนๆกัน  โดยถ้าหากนำจานที่มีน้ำหนักมากกว่ามาวางบนจานที่มีน้ำหนักน้อยกว่า จะทำให้จานที่มีน้ำหนักน้อยกว่า แตก !!! และจะแตกไปเรื่อยๆจนกว่าจานใบด้านล่างจะมีน้ำหนักเท่ากันหรือมากกว่า หรือจนกว่าจะไม่มีจานด้านล่างมารองรับแล้ว

ให้น้องๆเขียนโปรแกรมอ่านลำดับของจานที่กฤษฎาได้วางลงไปโดยให้ใส่จานทีละใบ  ซึ่งรวมถึงขนาดของจานและความถี่ของจาน  จากนั้นให้หาว่าลำดับของความถี่ของจานที่ได้ยินเมื่อวางจานลงไปตามนั้นแล้วจะเป็นเช่นใด

อธิบาย Input : จะมีแค่รูปแบบเดียวคือ   < a  b >  โดยที่  a = น้ำหนักของจาน  ,  b = ความถี่ของจาน

Enter Input : 1 10,5 20,3 30,3 40,4 50
10
40
30

'''