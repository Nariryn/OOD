'''
หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   
Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  ผิดทั้งหมดกฤษฎาได้กล่าวไว้  
เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน 
โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  A B B B A  -> A A 
เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  
โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา

  โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงลำดับของสีที่เหลือจากขวาไปซ้าย

1. Enter Input : G H H H H P
    3
    PHG
2. Enter Input : L C C X X X C D
    2
    DL
    Combo : 2 ! ! !
3. Enter Input : C C C
    0
    Empty
'''
class Stack:
    def __init__(self):
        self.item = []
        
    def pop(self):
        if self.is_Empty():
            return -1
        return self.item.pop()
    
    def is_Empty(self):
        return len(self.item) == 0
    
    def push(self,new):
        self.item.append(new)

    def size(self):
        return len(self.item)
    
    def __str__(self) -> str:
        return ''.join(self.item)
    
row = input('Enter Input : ').split()
combo = 0
aws = Stack()
for i in range(len(row)):
    if aws.size()>=2:
        a = aws.pop()
        b = aws.pop()
        if a == b and b == row[i]:
            combo += 1
        else:
            aws.push(b)
            aws.push(a)
            aws.push(row[i])
    else:
        aws.push(row[i])

print(aws.size())
if aws.size() > 0:
    print(aws)
else:
    print("Empty")
if combo > 1:
    print(f'Combo : {combo} ! ! !')

