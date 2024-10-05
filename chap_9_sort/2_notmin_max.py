def sort_by_frequency(freq_dict):
    sorted_dict = {}
    while freq_dict:
        max_key = max(freq_dict, key=freq_dict.get)
        sorted_dict[max_key] = freq_dict.pop(max_key)
    return sorted_dict

def count_frequencies(numbers):
    freq_dict = {}
    for num in numbers:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    return freq_dict

inp = [int(e) for e in input("Enter list  of numbers: ").split()]

freq_dict = count_frequencies(inp)

sorted_freq_dict = sort_by_frequency(freq_dict)

for num, freq in sorted_freq_dict.items():
    print(f"number {num}, total: {freq}")
