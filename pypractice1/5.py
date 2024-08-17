class MyInt:
    def __init__(self,number):
        self.num = number 
    
    def toRoman(self):
        num = [1, 4, 5, 9, 10, 40, 50, 90,
            100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        preresult = []
        new_num = self.num
        while new_num:
            div = new_num // num[i]
            new_num %= num[i]
    
            while div:
                preresult.append(sym[i])
                div -= 1
            i -= 1
        result = ''.join(preresult)
        return result
    
    def __add__(self,num2):
        return int(self.num + num2.num + (self.num + num2.num)/2)
    
print(' *** class MyInt ***')     
x,y = input('Enter 2 number : ').split()

a = MyInt(int(x))

b = MyInt(int(y))

print(f'{a.num} convert to Roman : {a.toRoman()}')

print(f'{b.num} convert to Roman : {b.toRoman()}')

print(f'{a.num} + {b.num} = {a+b}')



 