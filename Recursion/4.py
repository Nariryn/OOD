def countF(list,index, char,count):
    
    if len(list) <= index:
        return count
    elif list[index] != char:
        return count
    else:
        return countF(list,index+1,char,count+1)

def countB(list,index,char,count):
    if index < 0:
        return count
    elif list[index] != char:
        return count
    else:
        return countB(list,index-1,char,count+1)


l,ind = input("input number : ").split(",")
index = int(ind)
count = 0
countb = 0
if index < 1:
    print("Output : Pin number less than 1")
elif len(l) == 0:
    print("Output : List is entry")
elif len(l) < index:
    print("Output : Pin number out of range")
else:
    print(f'Character : {l[int(ind)-1]}')
    count = countF(l,index,l[index-1],count)
    count = countB(l,index-1,l[index-1],count)
    print(f"Count : {count}")