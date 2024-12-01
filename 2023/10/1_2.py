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
        

pipes:list[list[Tile]] = [[]]


max_y = 0

for y, line in enumerate(data):
    pipes.append([])
    
    for x, p in enumerate(line):
            
        pipes[y].append(Tile(p, None, x, y))
        
    max_y = y


animal = None

# for p in pipes:
#     if p.type == "S":
#         animal = p
#         break

# print(animal)

lookfor:list[tuple[int, int]] = []

print(len(pipes))
print(len(pipes[58]))

# y THEN x

lastpipe = pipes[58][51] # animal
currentpipe = pipes[58][50] # next pipe

travelled = []


while True:
    
    pipe = currentpipe
    
    # print("Current pipe", pipe)
    # print("Last pipe", lastpipe)
    # print()
    
    # print(pipe)
    
    if pipe.type == "S":
        break

    assert pipe.type != "."
    
    lookfor = []
        
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
    
    
    assert len(lookfor) == 2
    for p in lookfor:
        if p[0] == lastpipe.x and p[1] == lastpipe.y:
            pass
        else:
            selectedpipe = pipes[p[1]][p[0]]
    
    travelled.append(lastpipe)
    lastpipe = currentpipe
    currentpipe = selectedpipe
    
    
    if False:
        for y in range(max_y+1):
            
            for pipe_arr in pipes:
                
                for pipe2 in pipe_arr:
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
    
# print(travelled)
print("TRAVEL / 2")
print((len(travelled) + 1)/2)