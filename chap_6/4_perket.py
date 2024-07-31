def find_min_dif(mixer, index=0, cur_sour=1, cur_bitter=0, used=False):
    if index == len(mixer):
        if not used:
            return float('inf')
        return abs(cur_sour - cur_bitter)
    
    min_diff = find_min_dif(mixer, index + 1, cur_sour, cur_bitter, used)
    
    new_sour = cur_sour * mixer[index][0]
    new_bitter = cur_bitter + mixer[index][1]
    min_diff = min(min_diff, find_min_dif(mixer, index + 1, new_sour, new_bitter, True))
    
    return min_diff

inp_str = input("Enter Input : ")
mixer_strs = inp_str.split(',')

mixer = []
for mixer_str in mixer_strs:
    S, B = map(int, mixer_str.split())
    mixer.append((S, B))

min_dif = find_min_dif(mixer)
print(min_dif)
