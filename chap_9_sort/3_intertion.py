def insertionSort(sorted_part:list,unsorted_part:list):
    if unsorted_part:
        num = unsorted_part.pop(0)
        sorted_part,index = _insertS(sorted_part,num,0)
        if unsorted_part:
            print(f'insert {num} at index {index} : {sorted_part} {unsorted_part}')
        else:
            print(f'insert {num} at index {index} : {sorted_part}')
        return insertionSort(sorted_part,unsorted_part)
    return sorted_part

def _insertS(sorted_part:list,num:int,index:int):
    if len(sorted_part) <= index:
        sorted_part.append(num)
        return sorted_part,index
    if sorted_part[index] > num:
        sorted_part.insert(index,num)
        return sorted_part,index
    sorted_part,index = _insertS(sorted_part,num,index + 1)
    return sorted_part,index 

inp = list(map(int,input("Enter Input : ").split()))
x = inp.pop(0)
inp = insertionSort([x],inp)
print("sorted")
print(inp)