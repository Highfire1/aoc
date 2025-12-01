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
    assert dir == "L" or dir == "R"
    distance = int(line[1:])
    m = Movement(dir, distance)
    movements.append(m)

    
dial = 50
count = 0

for m in movements:
    
    print(m)

    operand = 0
    
    if m.direction == "R":
        operand = 1
    elif m.direction == "L":
        operand = -1
        
    for i in range(m.distance):
        dial += operand
        
        if dial == 0:
            count += 1
            print("click")
            
        if dial == -1:
            dial = 99
        
        if dial == 100:
            dial = 0
            count += 1
            print("click")
        
            
    print(dial)
    

print(count)