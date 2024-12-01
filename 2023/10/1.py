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
    
    def __repr__(self) -> str:
        return f"{self.x} {self.y} {self.type} {self.distance}"

    def __str__(self) -> str:
        return repr(self)
        

pipes:list[Tile] = []

max_y = 0

for y, line in enumerate(data):
    
    for x, p in enumerate(line):
        pipes.append(Tile(p, None, x, y))
        
    max_y = y


animal = None

for p in pipes:
    if p.type == "S":
        animal = p
        break

print(animal)

lookfor:list[tuple[int, int]] = []

lookfor.append((animal.x + 1, animal.y))
lookfor.append((animal.x - 1, animal.y))
lookfor.append((animal.x, animal.y + 1))
lookfor.append((animal.x, animal.y + 1))

print(lookfor)

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
                
                # print(f"MATCH {pipe.x} {pipe.y}")
                
                if pipe.distance != None:
                    continue # break?
                
                if pipe.type == "S":
                    continue
                
                # if pipe.type == ".":
                #     continue
                
                pipe.distance = i
                
                if pipe.type == "|":
                    lookfor.append((pipe.x, pipe.y + 1))
                    lookfor.append((pipe.x, pipe.y -1 ))
                if pipe.type == "-":
                    lookfor.append((pipe.x + 1, pipe.y))
                    lookfor.append((pipe.x - 1, pipe.y))
                if pipe.type == "L":
                    lookfor.append((pipe.x, pipe.y - 1))
                    lookfor.append((pipe.x + 1, pipe.y))
                if pipe.type == "J":
                    lookfor.append((pipe.x, pipe.y - 1))
                    lookfor.append((pipe.x- 1, pipe.y))
                if pipe.type == "7":
                    lookfor.append((pipe.x - 1, pipe.y))
                    lookfor.append((pipe.x, pipe.y + 1))
                if pipe.type == "F":
                    lookfor.append((pipe.x, pipe.y + 1))
                    lookfor.append((pipe.x + 1, pipe.y))
                
                
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


for p in pipes:
    if p.distance != None:
        biggest = max(biggest, p.distance)
    

print(biggest)
    
        



