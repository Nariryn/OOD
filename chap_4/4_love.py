class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def __str__(self):
        result = []
        for a, l in self.queue:
            format_str = f"{a}:{l}"
            result.append(format_str)
        return ', '.join(result)
    def __len__(self):
        return len(self.queue)
    
# a = activity, l = location
    
class Love:
    def __init__(self):
        self.queue = Queue()
        self.activity = ["Eat", "Game", "Learn", "Movie"]
        self.location = ["Res.", "ClassR.", "SuperM.", "Home"]
    
    def add_day(self, activity, location):
        self.queue.enqueue((activity, location))
    
    def get_activity_location(self):
        result = []
        for a, l in self.queue.queue:
            activity = self.activity[a]
            location = self.location[l]
            format_str = f"{activity}:{location}"
            result.append(format_str)
        return result
    
def calculate_love(my_day, u_day):
    my_a, my_l = my_day
    u_a, u_l = u_day
    
    if my_a == u_a and my_l == u_l:
        return 4
    
    elif my_a == u_a:
        return 1
    
    elif my_l == u_l:
        return 2
    else:
        return -5
    
def process_inp (inp_str):
    me = Love()
    you = Love()
    days = inp_str.split(",")
    
    for day in days:
        my_info, you_info = day.split()
        my_a, my_l = map(int, my_info.split(':'))
        u_a, u_l = map(int, you_info.split(':'))
        
        me.add_day(my_a, my_l)
        you.add_day(u_a,u_l)
        
    print(f"My   Queue = {me.queue}")
    print(f"Your Queue = {you.queue}")
    print(f"My   Activity:Location = {', '.join(me.get_activity_location())}")
    print(f"Your Activity:Location = {', '.join(you.get_activity_location())}")

    total_socre = 0
    for i in range(len(me.queue.queue)):
        my_day = me.queue.queue[i]
        your_day = you.queue.queue[i]
        day_score = calculate_love(my_day, your_day)
        total_socre += day_score
        
    if total_socre >= 7:
        print(f"Yes! You're my love! : Score is {total_socre}.")
      
    elif 0 < total_socre < 7:
        print(f"Umm.. It's complicated relationship! : Score is {total_socre}.")
    else:
        print(f"No! We're just friends. : Score is {total_socre}.")
    
inp = input("Enter Input : ")
process_inp(inp)