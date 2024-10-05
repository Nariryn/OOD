def bubble_sort_recur(a, i, j, n):
    if j == n:
        i = i+1
        j = 0
    if i == n:
        return 
    if a[i] < a[j]:
        temp = a[j]
        # print(f"a j {temp}")
        a[j] = a[i]
        # print(f"a j = i {temp}")
        a[i] = temp
        # print(f"a i {temp}")
        bubble_sort_recur(a, i, j+1, n)
    else:
        bubble_sort_recur(a, i, j+1, n)
    return a

a_inp = list(map(int, input("Enter Input : ").split()))
# print(a_inp)
a = bubble_sort_recur(a_inp, 0, 0, len(a_inp))
print(a)