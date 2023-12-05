with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 
    
sum = 0

import sys
import os
import psutil

os_used = sys.platform
process = psutil.Process(os.getpid())  # Set highest priority for the python script for the CPU
if os_used == "win32":  # Windows (either 32-bit or 64-bit)
    process.nice(psutil.REALTIME_PRIORITY_CLASS)
elif os_used == "linux":  # linux
    process.nice(psutil.IOPRIO_HIGH)
else:  # MAC OS X or other
    process.nice(20)  

seeds = []

class seed:
    def __init__(self, number, range) -> None:
        self.number = number
        self.range = range      
        


class mapper:
    def __init__(self, destination, source, range) -> None:
        self.destination = destination
        self.source = source
        self.range = range
        
        self.offset = destination - source
        self.limit = source + range
        
    

seeds = data[0].split(": ")[1].split(" ")
seeds = list(map(int, seeds))

newseeds:list[seed] = []

for i in range(0, len(seeds), 2):
    newseeds.append(seed(seeds[i], seeds[i+1]))

seeds = newseeds

i = 3
line = ""

parsemaps:dict[str, list[mapper]] = {}
map = ""

for line in data:
    
    if "seeds" in line:
        continue
    
    if "map" in line:
        map = line
        continue
    
    if line == "":
        continue
    
    s = line.split(" ")
    
    if map not in parsemaps:
        parsemaps[map] = []
        
    parsemaps[map].append(mapper(int(s[0]), int(s[1]), int(s[2])))


for map in parsemaps:
    parsemaps[map] = sorted(parsemaps[map], key=lambda x: x.source)

newmap = []

for map in parsemaps:
    newmap.append(tuple(parsemaps[map]))
    
maps:tuple[tuple[mapper]] = tuple(newmap)

# print(seeds)
# print(maps)    

# seeds = [seeds[0]]

results = []

low = 999999999999999999

for s in seeds:
    
    print(f"seed: n:{s.number} r:{s.range}")
    
    lowest_value = 9999999999999999999999
    
    backtrack_available = 100000
    backtracking = 0
    
    i = s.number
    while i < s.number + s.range:
        
        value = i
        o_seed = i
                
        for map in maps:
            
            r = s.range
            
            for k, entry in enumerate(map):
                
                r = min(r, entry.range)
                # r = min (r, next)
                
                assert r > 0, r
                
                if value >= entry.source and value < entry.limit:
                    
                    value += entry.offset
                    break
        
        if value < lowest_value:
            
            print(f"LV found for {o_seed} at location {value}.")
            lowest_value = value
        
        if backtracking > 0:
            backtracking -= 1
            i += 1
            
        elif value < lowest_value + 5000:
            
            if backtrack_available != 0:
                print(f"Low map found ({value}) - backtracking.", backtrack_available)
            
            i += 1
            i -= backtrack_available
            backtracking = backtrack_available
            
            backtrack_available = 0
        
        elif backtrack_available < 10000:
            i += 1
            if backtrack_available < 10000:
                backtrack_available += 500
        
        else:
            i += 1000
            if backtrack_available < 10000:
                backtrack_available += 500
            
    
    results.append(lowest_value)



    
lowest = results[0]
for i in results:
    print(i)
    lowest = min(i, lowest)
print("Lowest:", lowest)