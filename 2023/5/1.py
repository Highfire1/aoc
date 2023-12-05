with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 
    
sum = 0


seeds = []

class mapper:
    def __init__(self, destination, source, range) -> None:
        self.destination = destination
        self.source = source
        self.range = range
        
    def __str__(self) -> str:
        return f"s:{self.source} d:{self.destination} r:{self.range}"
        
    def __repr__(self) -> str:
        return str(self)
    

seeds = data[0].split(": ")[1].split(" ")
seeds = list(map(int, seeds))

i = 3
line = ""

maps:dict[str, list[mapper]] = {}
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
    
    if map not in maps:
        maps[map] = []
        
    maps[map].append(mapper(int(s[0]), int(s[1]), int(s[2])))
    

print(seeds)
# print(maps)    

# seeds = [seeds[0]]

results = []

for seed in seeds:
    
    # print("seed:", seed)
    
    value = seed
    
    for map in maps:
        
        for entry in maps[map]:
            
            if value >= entry.source and value <= entry.source + entry.range:
                
                offset = value - entry.source
                value = entry.destination + offset
                # print("match", entry, offset)

                break
            
        # print(map)
        # print(maps[map])
        
    results.append(value)
    print(value)


lowest = results[0]
for i in results:
    if i < lowest:
        lowest = i
        
print(i)