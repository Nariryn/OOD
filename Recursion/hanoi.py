# def hanoi(n,f,t,a):
#     if n == 0:
#         return
#     hanoi(n-1,f,a,t)
#     print("Move",n,"from",f,"to",t)
#     hanoi(n-1,a,t,f)
def hanoi(n,f,t,a):
    if n == 0:
        return
    hanoi(n-1,f,a,t)
    print("move",n,"from",f,"to",t)
    hanoi(n-1,a,t,f)

num = input("enter num : ")
num = int(num)
hanoi(num,"A","C","B")   

