def insertionSortRecursive(arr,n):
    if n<=1:
        return

    insertionSortRecursive(arr,n-1)
    last = arr[n-1]
    j = n-2
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1]=last
    if len(arr) == n:
        print(f'insert {last} at index {j+1} : {arr[:n]}')
    else:
        print(f'insert {last} at index {j+1} : {arr[:n]} {arr[n:]}')

inp = [int(i) for i in input("Enter Input : ").split(" ")]
n = len(inp)
insertionSortRecursive(inp,n)
print("sorted")
print(inp)