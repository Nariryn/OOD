'''
ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

***** อธิบาย Test Case 2:
Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value

'''

def get_first_greater_value(inp_lst, num):
    for value in inp_lst:
        if value > num:
            return value
        
    return -1


inp_data, inp_num = input("Enter Input : ").split("/")
lst_data = sorted(list(map(int, inp_data.split())))
lst_num = list(map(int, inp_num.split()))
for i in lst_num:
    first_greater_value = get_first_greater_value(lst_data, i)
    if first_greater_value == -1:
        print('No First Greater Value')
    else:
        print(first_greater_value)