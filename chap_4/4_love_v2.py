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
            formatted_string = f"{a}:{l}"
            result.append(formatted_string)
        return ', '.join(result) 
    
    def __len__(self):
        return len(self.queue)

class Student:
    def __init__(self):
        self.queue = Queue()
        self.activities = ["Eat", "Game", "Learn", "Movie"]
        self.locations = ["Res.", "ClassR.", "SuperM.", "Home"]

    def add_day(self, activity, location):
        self.queue.enqueue((activity, location))

    def get_activity_location(self):
        result = []  
        for a, l in self.queue.queue:
            activity = self.activities[a]
            location = self.locations[l]
            formatted_string = f"{activity}:{location}"
            result.append(formatted_string)
        return result


def calculate_score(my_day, your_day):
    my_activity, my_location = my_day
    your_activity, your_location = your_day
    
    if my_activity == your_activity and my_location == your_location:
        return 4
    elif my_activity == your_activity:
        return 1
    elif my_location == your_location:
        return 2
    else:
        return -5

def process_input(input_str):
    me = Student()
    you = Student()
    days = input_str.split(',')
    
    for day in days:
        my_info, your_info = day.split()
        my_activity, my_location = map(int, my_info.split(':'))
        your_activity, your_location = map(int, your_info.split(':'))
        
        me.add_day(my_activity, my_location)
        you.add_day(your_activity, your_location)
    
    print(f"My Queue = {me.queue}")
    print(f"Your Queue = {you.queue}")
    print(f"My Activity:Location = {', '.join(me.get_activity_location())}")
    print(f"Your Activity:Location = {', '.join(you.get_activity_location())}")
    
    total_score = 0
    for i in range(len(me.queue.queue)):
        my_day = me.queue.queue[i]
        your_day = you.queue.queue[i]
        day_score = calculate_score(my_day, your_day)
        total_score += day_score

    
    if total_score >= 7:
        print(f"Yes! You're my love! : Score is {total_score}.")
    elif 0 < total_score < 7:
        print(f"Umm.. It's complicated relationship! : Score is {total_score}.")
    else:
        print(f"No! We're just friends. : Score is {total_score}.")

inp = input("Enter Input : ")
process_input(inp)
