import math
import sys

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
    


traversing:list = []

i = 0
steps = 0
node = "AAA"

# print(directions)

for j in indexes:
    if j[2] == "A":
        traversing.append(j)

cycles = [[] for _ in range(len(traversing))]


for d_i, d in enumerate(traversing):
    print(d)
    # input()
    
    def dirtonum(d2):
        if d2 =="R":
            return 1
        return 0
    
    # print(directions[d])
    # input()
    i = 0
    sum = 0
    
    
    next = directions[d][dirtonum(instructions[i])]
    
    print()

    while True:
        # print(next)
        # input()
        
        
        i += 1
        if i >= len(instructions):
            i = 0
        sum += 1
        
        # print(i, instructions[i], next, directions[next])
        
        dir = dirtonum(instructions[i])

        next = directions[next][dir]
        
        # print(next)
        # input()
        
        # if next in seen:
        #     break
        
        # if sum == 10000:
        #     break
            
        if len(cycles[d_i]) >= 2:
            break
        # seen.append(next)
        

        # print(next[2],"???")
        
        if next[2] == "Z":
            print(d_i)
            cycles[d_i].append(sum)
            
        # print(directions[next])
        # if next[2] == "Z":
        #     break
        
        # print(next, d)
        
        


        
print(cycles)

intervals = []

interval = 0
last = 0
for i, t in enumerate(cycles):
    
    # print(len(cycles[i]), t[100], i)

    
    intervals.append(t[-1] - (t[-2]))
    

print(intervals)        
    

print(math.lcm(*intervals) )
    
    
    
sys.exit()
        


print(traversing)

lowest_total = 9999

while True:
    
    move = instructions[i]
    
    for j, node in enumerate(traversing):
        
        if move == "R":
            dest = directions[node][1]
        
        else:
            dest = directions[node][0]
            
        traversing[j] = dest
    
    i += 1
    steps += 1
    
    if i >= len(instructions):
        i = 0
            
    end = 0
    for j in traversing:
        # print(j)
        if j[2] == "Z":
            end += 1
    
    if end >= len(traversing) / 2:
        print("CLOSE")
        
    
    if end == len(traversing):
        break
    
    if steps % 100000 == 0:
        print(steps, end)
        
    
      
print(steps)
    
    