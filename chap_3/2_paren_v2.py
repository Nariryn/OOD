str = input("Enter expresion : ")
def paren(str):
    open_close = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    stack = []
    for i in str:
        if i in open_close.keys():
            stack.append(i)
        elif i in open_close.values():
            if not stack:
                return (f"{str} close paren excess")
            checker = open_close[stack.pop()]
            if checker != i:
                return(f"{str} Unmatch open-close")
    if stack:
        return(f"{str} open paren excess   {len(stack)} : {''.join(stack)}")
    return(f"{str} MATCH")

print(paren(str))