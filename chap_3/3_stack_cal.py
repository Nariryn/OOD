class Stack:
    def __init__(self, ls=None):
        if ls is None:
            self.stack = []
        else:
            self.stack = list

    # Push
    def push(self, i):
        self.stack.append(i)

    # Pop
    def pop(self):
        return self.stack.pop()

    # Peek
    def peek(self):
        return self.stack[-1]

    # isEmpty
    def isEmpty(self):
        if not self.stack:
            return False
        else:
            return True

    # Size
    def size(self):
        return len(self.stack)


def postFixeval(exp):
    s = Stack()
    op = ["+", "-", "*", "/"]
    for i in exp:
        if i not in op:
            s.push(int(i))
        else:
            result = 0
            if i == op[0]:
                result += s.peek()
                s.pop()
                result += s.peek()
                s.pop()
                s.push(result)
            elif i == op[1]:
                result = s.peek()
                s.pop()
                result -= s.peek()
                s.pop()
                s.push(-result)
            elif i == op[2]:
                result = 1
                result *= s.peek()
                s.pop()
                result *= s.peek()
                s.pop()
                s.push(result)
            elif i == op[3]:
                result = s.peek()
                s.pop()
                eiei = s.peek() / result
                s.pop()
                s.push(eiei)
    return s.peek()


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

print("Answer : ", '{:.2f}'.format(postFixeval(token)))


'''
จงเขียนโปรแกรมโดยใช้ Stack เพื่อคำนวณหา ค่าของนิพจน์แบบ postfix 

โดยให้แสดงผลลัพธ์ตามตัวอย่าง



class Stack():

    def __init__(self, ls = None):

    def push(self,i):

    def pop(self):

    def isEmpty(self):

    def size(self):

def postFixeval(st):

    s = Stack()

    ### Enter Your Code Here ###

    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))



testcase 1
 ***Postfix expression calcuation***
Enter Postfix expression : 6 5 2 3 + 8 * - 3 + *
Answer :  -192.00


testcase 2
 ***Postfix expression calcuation***
Enter Postfix expression : 4 22 * 89 / 98 * 21 - 32 2 / 4 * 10 / 23 * + 23 -48 * -
Answer :  1327.10


testcase 3
 ***Postfix expression calcuation***
Enter Postfix expression : 5 8 * 5 6 * 6 6 4 * - 5 6 * 6 / + - -
Answer :  -3.00

testcase 4
 ***Postfix expression calcuation***
Enter Postfix expression : 3 8 2 / 6 * 5 6 - + 6 6 -5 5 * 2 - - + + +
Answer :  65.00

'''