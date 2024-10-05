def bi_search(low, high, arr, x):
    while low <= high:
        mid = low + (high - low)//2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid -1
    return -1

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
result = bi_search(0, len(arr) - 1, sorted(arr), k)
if result != -1:
    print ("True")
else:
    print("False")
    
    
'''
ให้น้องๆเขียน Binary Search โดยใช้ Recursive เพื่อหาว่ามีค่านั้นอยู่ใน list หรือไม่ ถ้าหากมีให้ตอบ True หากไม่มีให้ตอบ False

***** อธิบาย Input
1. ด้านซ้าย  จะเป็น list ของ Data
2. ด้านขวา   จะเป็นค่าที่เราต้องการจะหา

testcase  1
Enter Input : 33 2 11 82 77 28 15 76 9 64/28
True

testcase 2
Enter Input : 33 2 11 82 77 28 15 76 9 64/50
False


'''