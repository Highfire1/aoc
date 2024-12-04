
data = []


find = "XMAS"


real_width = 0
real_height = 0
with open("input.txt", "r") as fi:
    for l in fi.readlines():
        real_height += 1
        data.append(list(l.replace("\n", "")))

real_width = len(data[0])

final_width = len(find)*2+real_width

# pad sides
for i in range(real_height):
    
    for j in range(len(find)):
        data[i].insert(0, " ")
        data[i].append(" ")



# pad top and bottom
for i in range(len(find)):
    data.insert(0, [" "]*final_width)
    data.append([" "]* final_width)
    

for l in data:
    print(l)


sw = len(find)
sh = len(find)


def search_for_word(arr:list[list], x:int, y:int) -> int:
    l = len(find)
    w_found = 0
    matches = [""] * 8
    # try all 8 directions
    
    # right
    for i in range(x, x+l):
        matches[0] += arr[y][i]
        
    # left
    for i in range(x, x-l, -1):
        matches[1] += arr[y][i]
    
    # down
    for i in range(y, y+l):
        matches[2] += arr[i][x]
        
    #up
    for i in range(y, y-l, -1):
        matches[3] += arr[i][x]
    
    # diagonal up right
    j = y
    for i in range(x, x+l):
        matches[4] += arr[i][j]
        j += 1
        
    j = y  
    # diagonal down right
    for i in range(x, x+l):
        matches[5] += arr[i][j]
        j -= 1
    
    # diagonal up left
    j = y
    for i in range(x, x-l, -1):
        matches[6] += arr[i][j]
        j += 1
    
    # diagonal down left
    j = y
    for i in range(x, x-l, -1):
        matches[7] += arr[i][j]
        j -= 1
        
        
    for m in matches:
        # print(f"|{m}|")
        if m == find:
            w_found += 1
    # input()
        
    return w_found
    
num = 0

for i in range(sw, sw+real_width):
    for j in range(sh, sh+real_height):
        num += search_for_word(data, i, j)
        # print(data[i][j], end="")
    # print()

print(num)