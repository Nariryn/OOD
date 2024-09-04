def find_Max(A, n):
    if n == 1:
        return A[0]
    else:
        return max(A[n-1], find_Max(A, n-1))

A = list(map(int, input("Enter Input : ").split()))
n = len(A)
print (f"Max : {find_Max(A, n)}")