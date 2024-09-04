def find_sum(A):
    if len(A) == 1:
        return A[0]
    else:
        return A[0] + find_sum(A[1:])

A = list(map(int, input("Enter number : ")))
print (f"sum of this list of number is : {find_sum(A)}")