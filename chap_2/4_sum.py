def triple_sum (num, target):
    triple = []
    n = len(num)
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if num[i] + num[j] + num[k] == target and not [num[i],num[j],num[k]] in triple:
                    triple.append([num[i],num[j],num[k]])
    return triple


num = list(map(int, input("Enter Your List : ").split()))
num.sort()
target = 5

triple_sum = triple_sum(num, target)

if len(num) < 3:
    print ("Array Input Length Must More Than 2")
else:
    print (f"{triple_sum}")