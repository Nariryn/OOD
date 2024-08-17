def is_palindrome(str):
    if len(str) <= 1:
        return True
    if str[0] == str[len(str)-1]:
        return is_palindrome(str[1:len(str)-1])
    else:
        return False
    
    
inp = input("Enter Input : ")
if is_palindrome(inp):
    print (f"'{inp}' is palindrome")
else:
    print (f"'{inp}' is not palindrome")