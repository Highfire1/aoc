
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
    
    if arr[y][x] != "A":
        return False

    out = False
    
    # condition 1 of 4
    # actually these are flipped but it doesn't matter
    # M M
    # S S
    if arr[y+1][x-1] == "M" and arr[y+1][x+1] == "M" and \
        arr[y-1][x-1] == "S" and arr[y-1][x+1] == "S":
            out=True
    
    # S S
    # M M
    if arr[y+1][x-1] == "S" and arr[y+1][x+1] == "S" and \
        arr[y-1][x-1] == "M" and arr[y-1][x+1] == "M":
            out=True
    
    # M S
    # M S
    if arr[y+1][x-1] == "M" and arr[y+1][x+1] == "S" and \
        arr[y-1][x-1] == "M" and arr[y-1][x+1] == "S":
            out=True
    
    # S M
    # S M
    if arr[y+1][x-1] == "S" and arr[y+1][x+1] == "M" and \
        arr[y-1][x-1] == "S" and arr[y-1][x+1] == "M":
            out=True
    
    # print(out)
    # input()
    return out
    
num = 0

for i in range(sw, sw+real_width):
    for j in range(sh, sh+real_height):
        num += search_for_word(data, i, j)
        # print(data[i][j], end="")
    # print()

print(num)