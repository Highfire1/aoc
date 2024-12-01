import math
import sys

with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 

class Tile:
    def __init__(self, pipe, distance, x, y) -> None:
        
        self.type = pipe
        self.distance = distance
        self.x = x
        self.y = y
        
        self.inside = False
    
    def __repr__(self) -> str:
        return f"TILE: {self.x} {self.y} {self.type} {self.distance}"

    def __str__(self) -> str:
        return repr(self)
        

pipes:list[Tile] = []

max_y = 0

for y, line in enumerate(data):
    
    for x, p in enumerate(line):
        pipes.append(Tile(p, None, x, y))
        
    max_y = y

def findpipe(x, y) -> Tile | None:
    for pipe in pipes:
        if pipe.x == x and pipe.y == y:
            return pipe
    
    return None

animal = None

for p in pipes:
    if p.type == "S":
        animal = p
        break

print(animal)
animal.distance = 0

lookfor:list[tuple[int, int]] = []

lookfor.append((animal.x + 1, animal.y))
lookfor.append((animal.x - 1, animal.y))
lookfor.append((animal.x, animal.y + 1))
lookfor.append((animal.x, animal.y + 1))

# print(lookfor)

i = 1
j = 0



while True:
    j += 1
    
    # print(j)
    
    
    oldlookfor = lookfor.copy()
    lookfor = []
    
    for search in oldlookfor:
    
        for pipe in pipes:
            
            if pipe.x == search[0] and pipe.y == search[1]:
                
                # print(f"{j} MATCH {pipe.x} {pipe.y}")
                # input()
                
                if pipe.distance != None:
                    continue # break?
                
                # if pipe.type == "S":
                #     continue
                
                # assert pipe.type != "."
                
                if pipe.type == ".":
                    continue
                
                pipe.distance = i
                
                if pipe.type == "|":
                    lookfor.append((pipe.x, pipe.y + 1))
                    lookfor.append((pipe.x, pipe.y -1 ))
                elif pipe.type == "-":
                    lookfor.append((pipe.x + 1, pipe.y))
                    lookfor.append((pipe.x - 1, pipe.y))
                elif pipe.type == "L":
                    lookfor.append((pipe.x, pipe.y - 1))
                    lookfor.append((pipe.x + 1, pipe.y))
                elif pipe.type == "J":
                    lookfor.append((pipe.x, pipe.y - 1))
                    lookfor.append((pipe.x- 1, pipe.y))
                elif pipe.type == "7":
                    lookfor.append((pipe.x - 1, pipe.y))
                    lookfor.append((pipe.x, pipe.y + 1))
                elif pipe.type == "F":
                    lookfor.append((pipe.x, pipe.y + 1))
                    lookfor.append((pipe.x + 1, pipe.y))
                else:
                    pipe.distance = None
                
                
    oldlookfor = lookfor.copy()
    
    if j % 100 == 0 and False:
        for y in range(max_y+1):
            
            for pipe2 in pipes:
                if pipe2.y == y:
                    if pipe2.distance != None:
                        if pipe2.distance > 9:
                            print("!", end="")
                        else:
                            print(pipe2.distance, end="")
                    else:
                        print(pipe2.type, end="")
                    
            print()
        print(lookfor)
        # input()
    
    if len(lookfor) == 0:
        break  
                
    i += 1

biggest = 0



# for p in pipes:
#     if p.distance != None:
#         biggest = max(biggest, p.distance)
    

# print(biggest)


for p in pipes:
    
    if p.distance != None:
        continue
    
    x = p.x
    y = p.y
    
    print("tile information", x, y)
    
    add_up = []
    checks = 0
    
    next = p
    matchchecks = 0
    while next != None:
        last = next
        next = findpipe(next.x, next.y + 1)
        if next != None and next.distance != None:
                        
            if last.type != "|" or last is p:
                matchchecks += 1  
    checks += matchchecks % 2 == 1
    add_up.append(matchchecks)
    print("MC1", matchchecks)  
    
    next = p
    matchchecks = 0
    while next != None:
        last = next
        next = findpipe(next.x, next.y - 1)
        if next != None and next.distance != None:
            if last.type != "|" or last is p:
                matchchecks += 1   
    checks += matchchecks % 2 == 1
    add_up.append(matchchecks)
    print("MC2", matchchecks)
    
    next = p
    matchchecks = 0
    while next != None:
        last = next
        next = findpipe(next.x + 1, next.y)
        if next != None and next.distance != None:
            if last.type != "-" or last is p:
                matchchecks += 1  
    checks += matchchecks % 2 == 1
    add_up.append(matchchecks)
    print("MC3", matchchecks)  
    
    next = p
    matchchecks = 0
    while next != None:
        last = next
        next = findpipe(next.x - 1, next.y)
        if next != None and next.distance != None:
            if last.type != "-" or last is p:
                matchchecks += 1   
    checks += matchchecks % 2 == 1
    add_up.append(matchchecks)
    print("MC4", matchchecks)  
    

    
    print(set(add_up))
    print(checks)
    # input()
    
    if checks == 4:
        p.inside = True
    
sum = 0

for y in range(max_y+1):
    
    for pipe2 in pipes:
        if pipe2.y == y:
            if pipe2.inside:
                print(" ", end="")
           
            elif pipe2.distance != None:
                print("!", end="")
                
            else:
                print(pipe2.type, end="")
            
    print()
    
for p in pipes:
    if p.inside:
        sum += 1
        
print("SUM:")
print(sum)
    
    
    

        



