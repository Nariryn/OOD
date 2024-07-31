class Node :
    def __init__ (self,element) :
        self.element = element
        self.next = None 
        self.previous = None

class LinkList :
    def __init__(self) :
        self.head = None
        self.tail = None

    def append(self,data) :
        new = Node(data)
        if self.head == None :
            self.head = new
            self.tail = new
        else :
            x = self.head
            while x.next != None :
                x = x.next
            x.next = new
            new.previous = x
            self.tail = new

    def __str__(self, seperator=" ") :
        x = self.head
        while x != None :
            if x.next != None :
                print(x.element,end=seperator)
            else :
                print(x.element,end=" ")
            x = x.next

    def isEmpty(self):
        return self.head == None

    def size(self) :
        j = self.head
        count = 0
        while j != None :
            j = j.next
            count += 1
        return count
    
    def insert_sort(self, data):
        new = Node(data)
        if self.head == None :
            self.head = new
            self.tail = new
        else :
            x = self.head
            while x != None:
                if x.element > new.element:
                    if x == self.head:
                        new.next = x
                        x.previous = new
                        self.head = new
                    else:
                        x.previous.next = new
                        new.previous = x.previous
                        new.next = x
                        x.previous = new
                    return
                else:
                    x = x.next
            self.append(data)

    
    def Radix_Sort (self,inp) :
        list0 = LinkList()
        list1 = LinkList()
        list2 = LinkList()
        list3 = LinkList()
        list4 = LinkList()
        list5 = LinkList()
        list6 = LinkList()
        list7 = LinkList()
        list8 = LinkList()
        list9 = LinkList()
        Before = LinkList()
        After = LinkList()
        linkedList = [list0, list1, list2, list3, list4, list5, list6, list7, list8, list9]

        for i in inp :
            Before.append(int(i))
        
        count = 1
        x = Before.head
        while True:
            while x != None :
                modder = 10 ** count
                divider = modder / 10
                moddedNumber = (abs(x.element) % modder) // divider
                if moddedNumber == 0 :
                    list0.insert_sort(x.element)
                elif moddedNumber == 1 :
                    list1.insert_sort(x.element)
                elif moddedNumber == 2 :
                    list2.insert_sort(x.element)
                elif moddedNumber == 3 :
                    list3.insert_sort(x.element)
                elif moddedNumber == 4 :
                    list4.insert_sort(x.element)
                elif moddedNumber == 5 :
                    list5.insert_sort(x.element)
                elif moddedNumber == 6 :
                    list6.insert_sort(x.element)
                elif moddedNumber == 7 :
                    list7.insert_sort(x.element)
                elif moddedNumber == 8 :
                    list8.insert_sort(x.element)
                else :
                    list9.insert_sort(x.element)
                x = x.next
            print("------------------------------------------------------------")
            print("Round :",count)
            for i in range(0, 10):
                print(i,":", end=' ')
                linkedList[i].__str__()
                print()
            if list0.size() == Before.size():
                break
            After = LinkList()
            for i in range (0, 10):
                t = linkedList[i].head
                while t != None:
                    After.append(t.element)
                    t=t.next
            # After.__str__()
            x = After.head
            for i in range(0, 10):
                linkedList[i].head = None
            count+=1
        print("------------------------------------------------------------")
        print(count-1, "Time(s)")
        print("Before Radix Sort : ", end="")
        Before.__str__(" -> ")
        print()
        print("After  Radix Sort : ", end="")
        list0.__str__(" -> ")
        print()

            
list = LinkList()
inp = input("Enter Input : ").split()

list.Radix_Sort(inp)