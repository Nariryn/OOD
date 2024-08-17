inp = [int(i) for i in input("Enter Input: ").split(" ")]
inp2 = inp.copy()
ans1 = []
ans2 = []
while len(inp2)>=2:
    inp2.sort(reverse=True)
    first = inp2.pop()
    second = inp2.pop()
    ans2.append(first+second)
    inp2.append(first+second)

while len(inp)>=2:
    inp.sort()
    first = inp.pop()
    second = inp.pop()
    ans1.append(first+second)
    inp.append(first+second)

print(f'Min cost: {sum(ans2)}')
print(f'Max cost: {sum(ans1)}')
