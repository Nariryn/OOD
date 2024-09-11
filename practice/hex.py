import random

# Generate two random 8-bit binary numbers
bin_num1 = random.randint(0, 255)  # 8-bit range: 0 to 255
bin_num2 = random.randint(0, 255)

# Display the binary numbers
print(f"First binary number : {bin(bin_num1)[2:].zfill(8)}")
print(f"Second binary number: {bin(bin_num2)[2:].zfill(8)}")

# Add the two numbers
result = bin_num1 + bin_num2

# Display the result in hexadecimal
inp = input("Enter a to continue: ")
if inp == 'A' or inp == 'a':
    print(f"Result in hexadecimal: {hex(result)}")
    
