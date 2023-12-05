with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 

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

# parse maps from data
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

# sort the maps in order
for map in parsemaps:
    parsemaps[map] = sorted(parsemaps[map], key=lambda x: x.source)

# make maps tuples for performance (?) idk if this helps
newmap = []

for map in parsemaps:
    newmap.append(tuple(parsemaps[map]))
    
maps:tuple[tuple[mapper]] = tuple(newmap)


# begin search
results = []

# general approach:
# search by thousand, which is mildly performant 
# when we see a low value, backtrack 10000 steps and only fully check that section
# after that is done we return to checking by thousand
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
            
            for entry in map:
                
                r = min(r, entry.range)
                assert r > 0, r
                
                if value >= entry.source and value < entry.limit:
                    
                    value += entry.offset
                    break
        
        # backtracking logic
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




print("RESULTS:")
lowest = results[0]
for i in results:
    print(i)
    lowest = min(i, lowest)
print("Lowest:", lowest)