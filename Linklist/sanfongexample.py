class Node:
    def __init__(self, val=None, next: 'Node' = None):
        self.val = val
        self.next = next
        self.visited = False
        self.ref_count = 0

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
        if new_head is not None:
            new_head.ref_count -= 1
            self.next = None
        return self, new_head
    
    def append(self, new_node):
        if self is None:
            return new_node
        temp = self
        while temp.next is not None:
            temp = temp.next
            if  temp is not None:
                temp.ref_count += 1
        temp.next = new_node
        return self
    
    def print(self):
        temp, result = self, ""
        while temp is not None:
            result += str(temp.val)
            temp = temp.next
            if temp is not None:
                result += ' -> '
        return result
def __repr__(self) -> str:
        return f"Node({self.val}, size={self.size()})"

def main():
    inp = [list(map(int, p.split('>'))) for p in input("Enter edges: ").split(',')]
    d: dict[int, Node] = {}
    for h, t in inp:
        d.setdefault(h, Node(h)).next = d.setdefault(t, Node(t))
        d[t].ref_count += 1
    tails = list(map(lambda a: a[1], inp))
    intersect: list[Node] = sorted(map(lambda n: d[n], set(filter(lambda n: tails.count(n) > 1, tails))), key=lambda n: n.val)
    if not intersect:
        return print("No intersection")
    print(*intersect, "Delete intersection then swap merge:", sep='\n')
    all_nodes = list(d.values())
    for n in filter(lambda n: n.next in intersect, all_nodes):
        n.next.ref_count -= 1
        n.next = None
    for n in intersect:
        if n.next is not None:
            n.next.ref_count -= 1
            n.next = None
    sll: list[Node] = sorted(filter(lambda n: n.ref_count == 0 and n not in intersect, all_nodes), key=lambda n: n.val)
    merged = None
    while sll:
        out, sll[0] = sll[0].dequeue()
        merged = Node.append(merged, out)
        head = sll.pop(0)
        if head is not None:
            sll.append(head)
    print(merged.print())

main()
