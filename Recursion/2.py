def deleteIsland(Map,y,x):
    if y<0 or x<0 or y>=len(Map) or x>= len(Map[0]) or Map[y][x]=='.':
        return Map
    Map[y][x] = '.'
    Map = deleteIsland(Map,y-1,x)
    Map = deleteIsland(Map,y,x+1)
    Map = deleteIsland(Map,y+1,x)
    Map = deleteIsland(Map,y,x-1)
    return Map

def countIsland(Map):
    count = 0
    for i in range(len(Map)):
        for j in range(len(Map[0])):
            if Map[i][j] == '#':
                count += 1
                Map = deleteIsland(Map, i, j)
    return count

h,w = input('Enter input: ').split()
screen = []
for i in range(int(w)):
    screen.append(input().split())

print(countIsland(screen))

        
