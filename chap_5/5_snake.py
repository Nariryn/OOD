class Node:
    def __init__(self, item) -> None:
        self.value = item
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, head = None) -> None:
        self.head = head
        self.tail = head

    def __str__(self) -> str:
        if self.isEmpty():
            return 'Empty'
        n = self.head
        tmp = [f'({n.value})']
        while n != self.tail:
            n = n.next
            tmp.append(f'{n.value}')
        if self.head == self.tail:
            tmp.append('Empty')
        return '->'.join(tmp)

    def reverse(self) -> str:
        if self.isEmpty():
            return 'Empty'
        n = self.tail
        tmp = [f'({n.value})']
        while n != self.head:
            n = n.prev
            tmp.append(n.value)
        if self.head == self.tail:
            tmp.append('Empty')
        return '->'.join(tmp)

    def swap(self):
        n = self.head.next
        while n:
            n1 = n
            n2 = n.next
            if not n2:
                self.remove_last()
                break
            prev_n1 = n1.prev
            nxt_n2 = n2.next

            prev_n1.next = n2
            n2.prev = prev_n1

            n2.next = n1
            n1.prev = n2

            n1.next = nxt_n2
            if nxt_n2:
                nxt_n2.prev = n1
            else:
                self.tail = n1
            n = nxt_n2
        return f'Swap success!'

    def shake(self):
        thres = int(self.head.value)
        tmp = []
        n = self.head.next
        while n:
            if n.value > thres:
                # print(int(n.value), int(n.prev.value))
                tmp.append(n.value)
                n.prev.next = n.next
                if n.next:
                    n.next.prev = n.prev
                else:
                    self.tail = n.prev
            n = n.next
        return f'Shake success!->{tmp}'

    def remove_last(self):
          prev = self.tail.prev
          prev.next = None
          self.tail = prev

    def play(self, item):
        if self.weightSum() >= item:
            return 'Play success!->[]'
        n = self.tail
        eaten = []
        while n != self.head:
            if int(n.value) != 0 and item % int(n.value) == 0:
                for i in range(len(eaten)):
                    self.remove_last()
                return f'Play success!->{eaten[::-1]}'
            eaten.append(int(n.value))
            n = n.prev
        n.next.prev = self.tail
        self.tail.next = n.next
        self.tail.prev.next = n
        n.prev = self.tail.prev
        self.head = self.tail
        self.tail = n
        self.tail.next = None
        self.head.prev = None 
        return 'Play success!->[]'

    def weightSum(self):
        n = self.head
        sum = int(n.value)
        while n != self.tail:
            n = n.next
            sum += int(n.value)
        return sum

    def append(self, item):
        if self.isEmpty():
            self.head = Node(item)
            self.tail = self.head
            return
        t = self.tail
        t.next = Node(item)
        self.tail = t.next
        self.tail.prev = t
        return f'Steal success!->{item}'

    def isEmpty(self):
        return self.head == None
    
    def isDead(self):
        return self.head == self.tail


snake, opr = input('Snake Game : ').split('/')
snake = snake.split(' ')
opr = opr.split(',')

ll = LinkedList()
while snake:
    ll.append(int(snake.pop(0)))
print(ll)
if ll.isDead():
    print('Mom is dead')
else:
    for o in opr:
        if o.split(' ')[0] == 'SW':
            print(ll.swap())
            print(ll)
        elif o.split(' ')[0] == 'SH':
            print(ll.shake())
            print(ll)
        elif o.split(' ')[0] == 'F':
            n = o.split(' ')[1]
            print(ll.append(int(n)))
            print(ll)
        elif o.split(' ')[0] == 'D':
            n = o.split(' ')[1]
            print(ll.play(int(n)))
            print(ll)
        # print(ll.reverse())
        print('------------------------------')

        if ll.isDead():
            print('Mom is dead')
            break
print('Snake Game : ')