import math


with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 
    
sum = 0

indexes = []

directions:dict[str] = {}

instructions = data[0]

for line in data[2:]:
    
    s = line.split(" = ")
    
    rl = s[1].replace("(", "").replace(")", "").split(", ")
    
    directions[s[0]] = (rl[0], rl[1])
    
    indexes.append(s[0])
    

i = 0
steps = 0
node = "AAA"

# print(directions)

while True:
    
    move = instructions[i]
    
    # print(i, directions[node])
    
    
    if move == "R":
        dest = directions[node][1]
    
    else:
        dest = directions[node][0]
        
    node = dest
    i += 1
    steps += 1
    
    if node == "ZZZ":
        break
    
    if i >= len(instructions):
        i = 0
        
    if steps % 100000 == 0:
        print(steps)
      
    
print(steps)
    
    