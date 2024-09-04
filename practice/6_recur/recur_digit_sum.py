def find_sum_digit(n):
    if n < 10:
        return n
    else:
        return find_sum_digit(sum(map(int, str(n))))
        
    
A = int(input("Enter num : "))
result = find_sum_digit(A)

print (f"the sum : {result}")

