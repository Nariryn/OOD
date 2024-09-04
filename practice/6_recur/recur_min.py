def finMin(A, n):
    if (n == 1):
        return A[0]
    return min(A[n-1], finMin(A, n-1))

A = list(map(int, input("Enter Input : ").split()))
print(A)
n = len(A)
print(n)

print(f"Min : {finMin(A, n)}")