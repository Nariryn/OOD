class funString():

    def __init__(self,string = ""):
        self.string = string
        ### Enter Your Code Here ###

    def __str__(self):
        pass
        ### Enter Your Code Here ###

    def size(self) :
        return len(self.string)
        ### Enter Your Code Here ###

    def changeSize(self):
        ans = []
        for i in self.string:
            if i.isupper() == True:
                ans.append(i.lower())
            else:
                ans.append(i.upper())
        return ''.join(ans)
        ### Enter Your Code Here ###

    def reverse(self):
        return self.string[::-1]
        ### Enter Your Code Here ###

    def deleteSame(self):
        ans = []
        for i in self.string:
            if i not in ans:
                ans.append(i)

        return ''.join(ans)
       ### Enter Your Code Here ###



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())