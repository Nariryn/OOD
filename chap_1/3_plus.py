print (" *** Summation of each digit ***")

number = int(input("Enter a positive number : "))

if number < 0:
    print(f"{number} is invalid!")
else: 
    sum = sum(int(digit) for digit in str(number))
    print (f"Summation of each digit =  {sum}")