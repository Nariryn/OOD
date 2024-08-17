class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
        self.visited = False
        self.ref = 0
    
    def size(self):
        temp, count = self, 0
        while temp is not None and not temp.visited:
            temp.visited = True
            temp = temp.next
            count += 1
        temp = self
        while temp is not None and temp.visited:
            temp.visited = False
            temp = temp.next
        return count

    def dequeue(self):
        new_head = self.next
        return self, new_head
    
    def __repr__(self) -> str:
        return f"Node({self.value}, size={self.size()})"

inp = input("Enter edges: ").split(",")
inpdata = []
for i in inp:
    first,second = i.split('>')
    inpdata.append([int(first),int(second)])

dict_linklist = {}
for f,s in inpdata:
    if f not in dict_linklist:
        dict_linklist.update({f:Node(f)})
    
    if s not in dict_linklist:
        dict_linklist.update({s:Node(s)})
        dict_linklist[f].next = dict_linklist[s]
        dict_linklist[s].ref += 1
    
    else:
        dict_linklist[f].next = dict_linklist[s]
        dict_linklist[s].ref += 1

intersect = []

for key,value in dict_linklist.items():
    if value.ref > 1:
        intersect.append(value)
intersect.sort(key= lambda x:x.value)

if intersect == []:
    print("No intersection")
    exit()
else:
    for each in intersect:
        print(each)
print("Delete intersection then swap merge:")

for k,v in dict_linklist.items():
    if v.next != None and v.next.ref > 1:
        v.next = None
    
    if v.next != None and v.ref > 1:
        v.next.ref -= 1
        v.next = None

head = []
for key,value in dict_linklist.items():
    if value.ref == 0:
        head.append(dict_linklist[key])

head.sort(key= lambda x:x.value)
headdict = {}
for node in head:
    headdict.update({node.value: node})
ans = []

while headdict != {}:
    for key,value in headdict.items():
        if value != None:
            head , newhead = value.dequeue()
            ans.append(head)
            headdict[key] = newhead
    length = len(headdict)
    l = 0
    for key,value in headdict.items():
        if value == None:
            l += 1
    if l == length:
         break
s=''

for each in ans:
    s += str(each.value) + ' -> '

print(s[:-4])