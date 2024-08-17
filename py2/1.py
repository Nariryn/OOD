class Calculator :
    def __init__(self,number):
        self.num = number
    ### Enter Your Code Here ###

    def __add__(self,num2):
        return self.num + num2.num
        ###Enter Your Code For Add Number###

    def __sub__(self,num2):
        return self.num - num2.num
        ###Enter Your Code For Sub Number### 

    def __mul__(self,num2):
        return self.num * num2.num
        ###Enter Your Code For Mul Number###

    def __truediv__(self,num2):
        return self.num / num2.num
        ###Enter Your Code For Div Number###

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")