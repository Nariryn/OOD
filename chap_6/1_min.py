def findMin(A, n):
    if (n == 1):
        return A[0]
    return min(A[n-1], findMin(A, n-1))

A = list(map(int, input("Enter Input : ").split()))
n = len(A)

print(f"Min : {findMin(A, n)}")