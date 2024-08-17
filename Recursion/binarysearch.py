def searchR(low,high,x):
    if high<low:
        return -1
    mid = (low+high) //2
    if x == a[mid]:
        return mid
    elif a[mid]<x:
        return searchR(mid+1,high,x)
    else:
        return searchR(low,mid-1,x)
    
a = [0,1,2,3,4,5,6,7,8,9,10]
    