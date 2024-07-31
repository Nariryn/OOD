class DoublyLinkedlist:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None 
    
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        
    def append(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.head.prev = self.head
            self.head.next = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            tail.next.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self.size +=1
        
    def get_node(self, data):
        cur = self.head
        if cur is None:
            return "Not found"
        while True:
            if cur.data == data:
                return cur
            cur = cur.next
            if cur == self.head:
                break
        return "Not found"

    def find_route(self, start, end, direction =None):
        start_node = self.get_node(start)
        end_node = self.get_node(end)
        
        if start_node == "Not found" or end_node == "Not found":
            return "Invalid station name(s)"
        
        forward_count = 0
        backward_count = 0
        
        cur = start_node
        while cur != end_node:
            cur = cur.next
            forward_count += 1
            
        cur = start_node
        while cur != start_node:
            cur = cur.prev
            backward_count += 1

        if direction == 'F':
            route = []
            cur = start_node
            while cur != end_node:
                route.append(cur.data)
                cur = cur.next
            route.append(end_node.data)
            return ("Forward Route", route, forward_count)
        
        elif direction == 'B':
            route = []
            cur = start_node
            while cur != end_node:
                route.append(cur.data)
                cur = cur.prev
            route.append(end_node.data)
            return ("Backward Route", route, backward_count)
        
        else:
            if forward_count < backward_count:
                route = []
                cur = start_node
                while cur != end_node:
                    route.append(cur.data)
                    cur = cur.next
                route.append(end_node.data)
                return ("Forward Route", route, forward_count)
            elif forward_count > backward_count:
                route = []
                cur = start_node
                while cur != end_node:
                    route.append(cur.data)
                    cur = cur.next
                route.append(end_node.data)
                return ("Backward Route", route, backward_count)
            else:
                forward_route = []
                backward_route = []
                cur = start_node
                while cur != end_node:
                    forward_route.append(cur.data)
                    cur = cur.next
                forward_route.append(end_node.data)
                cur = start_node
                while cur != end_node:
                    backward_count.append(cur.data)
                    cur = cur.prev
                backward_route.append(cur.data)
                return (["Forward Route", forward_route], ["Backward Route", backward_route], forward_count)
                                
def process_route(station_inp,  route_inp):                                                       
    station_list  = station_inp.split(",")
    route_info = route_inp.split(",")
    start_station = route_info[0]
    end_station  = route_info[1]
    if len(route_info) > 2:
        direction = route_info[2]
    else:
        direction = None
    
    cdll = DoublyLinkedlist()
    for station in station_list:
        cdll.append(station)
    result = cdll.find_route(start_station, end_station, direction)
    if result == "Invalid station name(s)":
        print (result)
        return
    if isinstance(result[0], list):
        forward_result, backward_result, count = result
        print(f"{forward_result[0]}: {'->'.join(forward_result[1])},{count}")
        print(f"{backward_result[0]}: {'->'.join(backward_result[1])},{count}")
    else:
        route_type, route, count = result
        print(f"{route_type}: {'->'.join(route)},{count}")


print("***Railway on route***")
station_inp, dest_inp = input("Input Station name/Source, Destination, Direction(optional): ").split("/")
process_route(station_inp, dest_inp)