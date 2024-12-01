import math
import sys

with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 


print(data)


def insert_column(d, index):
    
    for i, row in enumerate(d):
        
        d[i] = row[0:index] + "." + row[index:]
    
def insert_row(d:list[str], index):
    
    d.insert(index, "." * len(d[0]))
    print(len(d))


# add rows
i = 0
while i < len(data):
    
    if data[i].count("#") == 0:
        insert_row(data, i)
        i += 2
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
        insert_column(data, i)
        i += 2
    else:
        i += 1

locations:list[tuple[int, int]] = []

for y, line in enumerate(data):
    
    for x, char in enumerate(line):
        
        if char == "#":
            locations.append((x, y))
            

print(locations)

distance = 0

for loc1 in locations:
    
    for loc2 in locations:
        
        if loc1 == loc2:
            continue
        
        if loc2[0] > loc1[0]:
            distance += loc2[0] - loc1[0]
        else:
            distance += loc1[0] - loc2[0]
            
        if loc2[1] > loc1[1]:
            distance += loc2[1] - loc1[1]
        else:
            distance += loc1[1] - loc2[1]
        
        
        
# (1, 6) -> (5, 11) = 9 
#  5-1 + 11-6 = 4+5 = 9

print(distance/2) # each path is counted twice