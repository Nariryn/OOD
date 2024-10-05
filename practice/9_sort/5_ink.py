
result, inp = input("Enter Input : ").split('/')

result = int(result)

inp = inp.split()
lst = [int(i) for i in inp]

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
                
    return lst

lst = bubble_sort(lst)

def get_combinations(lst, r):
    result = []

    def combine(data, start, end, index):
        if index == r:
            result.append(data[:])
            return
        for i in range(start, end + 1):
            data[index] = lst[i]
            combine(data, i + 1, end, index + 1)

    combine([None] * r, 0, len(lst) - 1, 0)
    return result

lst_combination = []

for i in range(len(lst)+1):
    lst_combination += get_combinations(lst, i)

have = False
for combi in lst_combination:
    if sum(combi) == result:
        have = True
        print(combi)

if not have:
    print("No Subset")
