def palindrome (str):
    if len(str) <= 1:
        return True
    elif str[0] == str[len(str)-1]:
        return palindrome(str[1:len(str)-1])
    else:
        return False

str = input("Enter Input : ")
if palindrome(str):
    print(f"'{str}' is palindrome")
else:
    print(f"'{str}' is not palindrome")