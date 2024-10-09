def bubble_sort_recur(a, i, j, n):
    if j == n:
        i = i+1
        j = 0
    if i == n:
        return 
    if a[i] < a[j]:
        #min to max
        temp = a[j]
        a[j] = a[i]
        a[i] = temp
        bubble_sort_recur(a, i, j+1, n)
    else:
        bubble_sort_recur(a, i, j+1, n)
    return a

a_inp = list(map(int, input("Enter Input : ").split()))
a = bubble_sort_recur(a_inp, 0, 0, len(a_inp))
print(a)

'''
เขียน function bubble sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

testcase 1
Enter Input : 4 3 2 1
[1, 2, 3, 4]

testcase 2
Enter Input : 3 2 1 5 6 7
[1, 2, 3, 5, 6, 7]

testcase 3
Enter Input : 1 2 3 4 5
[1, 2, 3, 4, 5]

'''