def swap(str,k):
    if len(str) > k:
        return str[k::-1] + swap(str[k+1:],k)
    return str[::-1]

s,n = input("enter s and n : ").split(',')
n = int(n)-1
print(swap(s,n))
