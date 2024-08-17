'''
ให้น้องๆเขียนโปรแกรมรับ input เป็นวงเล็บ โดยมีรูปแบบดังนี้  วงเล็บเปิด :  (  กับ  [    วงเล็บปิด :  )  กับ  ]   
โดยให้หาว่าถ้าหากนำวงเล็บมาจับคู่กัน จะครบทุกคู่หรือไม่  โดยให้แสดงผลลัพธ์ที่บอกว่าคู่วงเล็บที่ Input เข้ามานั้น Match กันหรือไม่
testcase
1.Enter Input : ()[]
  Parentheses : Matched ! ! !
2.Enter Input : [](]
  Parentheses : Unmatched ! ! !
'''

values = input('Enter Input : ')
count = {'(':0,')':0,'[':0,']':0}
err = 0
for i in values:
    if i in count:
        count[i] += 1
    else:
        err = 1

if count['('] == count[')'] and err == 0 and count['('] >0 and count['['] == count[']'] and count['[']>0:
    print('Parentheses : Matched ! ! !')
else:
    print('Parentheses : Unmatched ! ! !')