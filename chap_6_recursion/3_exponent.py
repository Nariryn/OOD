def generate_binary_numbers(n, prefix=''):
    if n == 0:
        print(prefix)
    else:
        generate_binary_numbers(n-1, prefix + '0')
        generate_binary_numbers(n-1, prefix + '1')


n = int(input("Enter Number : "))
if n < 0:
    print("Only Positive & Zero Number ! ! !")
elif n == 0:
    print("0")
else:
    generate_binary_numbers(n)


