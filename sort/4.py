def binarySearch(arr, item, low, high):
 
    if (low >= high):
        return (low + 1) if (item > arr[low]) else low
 
    mid = (low + high) // 2
 
    if (item == arr[mid]):
        return mid + 1
 
    if (item > arr[mid]):
        return binarySearch(arr, item, mid + 1, high)
 
    return binarySearch(arr, item, low, mid - 1)

def printMedian(arr, n):
 
    i, j, pos, num = 0, 0, 0, 0
    count = 1
 
    print(f"list = {arr[:1]} : median = {arr[0]}.0")
 
    for i in range(1, n):
        median = 0
        j = i - 1
        num = arr[i]
        pos = binarySearch(arr, num, 0, j)
        while (j >= pos):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = num

        count += 1

        if (count % 2 != 0):
            median = arr[count // 2] / 1
 
        else:
            median = (arr[(count // 2) - 1] + arr[count // 2]) / 2

        print(f"list = {ans[:i+1]} : median = {median}")

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "insertion sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    ans = l.copy()
    n = len(l)
    printMedian(l,n)