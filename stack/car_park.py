'''
ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก 
จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ 
ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม 
ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output

การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ 
จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ 
การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น 
เลขในตำแหน่งที่ 4

***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***

*** สามารถสร้างได้มากกว่า 1 stack ***
class Stack:

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()


m,n = int(m),int(n)

### Enter Your Code Here ###

1. ******** Parking Lot ********
Enter max of car,car in soi,operation : 5 1,2,3,4 arrive 5
car 5 arrive! : Add Car 5
[1, 2, 3, 4, 5]

2.******** Parking Lot ********
Enter max of car,car in soi,operation : 4 1,2,3,4 arrive 5
car 5 cannot arrive : Soi Full
[1, 2, 3, 4]

3.******** Parking Lot ********
Enter max of car,car in soi,operation : 5 1,2,3,4 arrive 1
car 1 already in soi
[1, 2, 3, 4]

4.******** Parking Lot ********
Enter max of car,car in soi,operation : 8 1,4,6,2,3,5,8 arrive 7
car 7 arrive! : Add Car 7
[1, 4, 6, 2, 3, 5, 8, 7]

5.******** Parking Lot ********
Enter max of car,car in soi,operation : 5 0 depart 3
car 3 cannot depart : Soi Empty
[]

6.******** Parking Lot ********
Enter max of car,car in soi,operation : 4 1,3,2 depart 1
car 1 depart ! : Car 1 was remove
[3, 2]

7.******** Parking Lot ********
Enter max of car,car in soi,operation : 6 2,3,5,7,8 depart 1
car 1 cannot depart : Dont Have Car 1
[2, 3, 5, 7, 8]

8.******** Parking Lot ********
Enter max of car,car in soi,operation : 5 7,3,2,1,4 depart 7
car 7 depart ! : Car 7 was remove
[3, 2, 1, 4]

9.******** Parking Lot ********
Enter max of car,car in soi,operation : 5 0 arrive 1
car 1 arrive! : Add Car 1
[1]

'''
class Stack:
    def __init__(self):
        self.item = []
    def push(self,new):
        self.item.append(new)
    def pop(self,new):
        wh = self.item.index(new)
        self.item.pop(wh)
    def setItem(self,new):
        if new == '0':
            self.item = []
        else:
            self.item = new.split(',')
            self.item = [int(item) for item in self.item]
        
carpark = Stack()
print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
### Enter Your Code Here ###
carpark.setItem(s)
if m > len(carpark.item) and o == 'arrive':
    if n in carpark.item:
        print(f'car {n} already in soi')
    else:
        carpark.push(n)
        print(f'car {n} arrive! : Add Car {n}')
elif m <= len(carpark.item) and o == 'arrive':
    if n in carpark.item:
        print(f'car {n} already in soi')
    else:
        print(f'car {n} cannot arrive : Soi Full')
elif o == 'depart' and len(carpark.item) == 0:
    print(f'car {n} cannot depart : Soi Empty')
elif o == 'depart' and len(carpark.item) > 0:
    if n in carpark.item:
        carpark.pop(n)
        print(f'car {n} depart ! : Car {n} was remove')
    else:
        print(f'car {n} cannot depart : Dont Have Car {n}')

print(carpark.item)


