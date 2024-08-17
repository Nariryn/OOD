def pantip(k,n,arr,path):
    numofpattern = 0
    if arr:
        if k - arr[n] == 0:
            path.append(arr[n])
            print(' '.join(map(str, path)))
            path.pop(-1)
            numofpattern += 1
        elif k - arr[n] > 0:
            path.append(arr[n])
            numofpattern += pantip(k - arr[n],n,arr[1:],path)
            path.pop(-1)
        return pantip(k,n,arr[1:],path) + numofpattern
    return numofpattern