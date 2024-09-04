def sum(n):
    if n < 10:
        return n
    else:
        digit_sum = sum(map(int, str(n)))
        return sum(digit_sum)
        
    
A = int(input("Enter num : "))
result = sum(A)

print (f"the sum : {result}")