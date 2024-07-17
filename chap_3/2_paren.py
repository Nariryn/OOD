open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

def check(myStr):
    stack = []
    excess_open = {}
    excess_close = {}
    
    for i in myStr:
        if i in open_list:
            stack.append(i)
            excess_open[i] = excess_open.get(i, 0) + 1
        elif i in close_list:
            pos = close_list.index(i)
            corresponding_open = open_list[pos]
            if len(stack) > 0 and stack[-1] == corresponding_open:
                stack.pop()
                excess_open[corresponding_open] -= 1
                if excess_open[corresponding_open] == 0:
                    del excess_open[corresponding_open]
            else:
                excess_close[i] = excess_close.get(i, 0) + 1
    
    if len(excess_open) == 0 and len(excess_close) == 0:
        return "MATCH"
    
    result = []
    if excess_open:
        for key, value in excess_open.items():
            result.append(f"open paren excess   {value} : {key * value}")
    if excess_close:
        result.append(f"close paren excess")
    
    return "Unmatch open-close" if result else "MATCH"

string = input("Enter expresion : ")
print(string, check(string))
