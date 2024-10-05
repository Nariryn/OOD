def get_median(int_list):
    middle_index_float = (len(int_list) - 1) / 2
    middle_index_int = int(middle_index_float)
    less_value = int_list[middle_index_int]
    if middle_index_float % 1 != 0:
        more_value = int_list[middle_index_int + 1]
        _median  = (less_value + more_value) / 2
        return _median
    
    return float(less_value)


def insertion_sort(int_list):
    for sort_range in range(1, len(int_list)):
        for current_index in range(sort_range, 0, -1):
            previous_index = current_index - 1
            if int_list[previous_index] < int_list[current_index]:
                break
            int_list[previous_index], int_list[current_index] = int_list[current_index], int_list[previous_index]

    return int_list

 
inp_val = [e for e in input("Enter Input : ").split()]
if inp_val[0] == 'EX':
    Ans = "insertion sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : " + Ans)
else:
    inp_val = list(map(int, inp_val))
    running_list = []
    for i, value in enumerate(inp_val):
        running_list.append(value)
        running_list = insertion_sort(running_list)
        median = get_median(running_list)
        sliced_list = inp_val[:i+1:]
        print(f'list = {sliced_list} : median = {median}')