import math
import sys

with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 


# print(data)

for i, row in enumerate(data):
    data[i] = list(row)


def change_column(d, index):
    
    for i, row in enumerate(d):
        
        d[i] = row[0:index] + ["|"] + row[index+1:]
    
def change_row(d:list[str], index):
    
    d[index] = ["_"] * len(d[0])
    # print(len(d))


# add rows
i = 0
while i < len(data):
    
    if data[i].count("#") == 0:
        change_row(data, i)
        i += 1
    else:
        i += 1




# add columns
i = 0
while i < len(data[0]):
    
    all_empty = True
    for row in data:
        if row[i] == "#":
            all_empty = False
            break
    
    if all_empty:
        change_column(data, i)
        i += 1
    else:
        i += 1

locations:list[tuple[int, int]] = []

for y, line in enumerate(data):
    
    for x, char in enumerate(line):
        
        if char == "#":
            locations.append((x, y))

# for row in data:
#     print("".join(row))            
# input()

# print(locations)

distance = 0

for loc1 in locations:
    
    for loc2 in locations:
        
        if loc1 == loc2:
            continue
    
        # x
        if loc2[0] > loc1[0]:
            biggerx = loc2[0]
            smallerx = loc1[0]
            
            starty = loc1[1]
            endy = loc2[1]
        else:
            biggerx = loc1[0]
            smallerx = loc2[0]
            
            starty = loc2[1]
            endy = loc1[1]
        
        # y
        if starty < endy:
            ydirection = "up"
        else:
            ydirection = "down"
        
        print(f"pair: {loc1}, {loc2}")
        print(smallerx, starty, biggerx, endy)
        
        
        pairdist = 0
        MULTIPLIER = 2
        
        x = smallerx
        y = starty
        while True:
            
            
            if y != endy:
                
                if ydirection == "up":
                    y += 1
                else:
                    y -= 1
                
                if data[y][x] == "!":
                    
                    pairdist += MULTIPLIER
                    # print("MULTIPLY", pairdist)
                else:
                    pairdist += 1
                
                # data[y][x] = "/"
            
            if x < biggerx:
                x += 1
                
                if data[y][x] == "!":
                    pairdist += MULTIPLIER
                    # print("MULTIPLY", pairdist)
                else:
                    pairdist += 1
                
                # data[y][x] = "/"
            
            distance += pairdist
            
            print(x, y)
            for row in data:
                print("".join(row))
            print(pairdist, distance)
            input()
            
            data[y][x] = "/"
            
            pairdist = 0
            
            if y == endy and x == biggerx:
                break
                
            

        
        
# (1, 6) -> (5, 11) = 9 
#  5-1 + 11-6 = 4+5 = 9

print(int(distance/2)) # each path is counted twice