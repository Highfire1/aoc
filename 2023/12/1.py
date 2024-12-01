import math
import sys

with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 



class Module:
    def __init__(self, type, name, destinations:list) -> None:
        self.type = type
        self.name = name
        self.destinations = destinations
        
    def __str__(self) -> str:
        return f"Name: {self.name} Type: {self.type} Dests: {self.destinations}"
    
    def __repr__(self) -> str:
        return str(self)

modules:dict[str, Module] = {}


for line in data:
    
    s = line.split(" -> ")
        
    if s[0][0] in "%&":
        m = Module(s[0][0], s[0][1:], s[1].split(","))
    else:
        m = Module(s[0], None, s[1].split(","))
        
    
    modules[m.name] = m
    

for m in modules:
    print(modules[m])
