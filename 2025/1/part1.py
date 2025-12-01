

from dataclasses import dataclass
from typing import Literal


with open("input.txt", "r") as f:
    DATA = f.read().splitlines()
    

@dataclass
class Movement:
    direction: Literal["R", "L"]
    distance: int

movements: list[Movement] = []  

for line in DATA:
    dir = line[0]
    distance = int(line[1:])
    m = Movement(dir, distance) # type: ignore
    movements.append(m)

    
dial = 50
count = 0

for m in movements:
    if m.direction == "R":
        dial += m.distance
    elif m.direction == "L":
        dial -= m.distance
    
    normalized = False
    while not normalized:
        if dial < 0:
            dial += 100
        elif dial > 99:
            dial -= 100
        else:
            normalized = True
        
    if dial == 0:
        count += 1
    
    print(m, dial)

print(count)