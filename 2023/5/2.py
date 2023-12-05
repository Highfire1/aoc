with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 
    
sum = 0


seeds = []

class seed:
    def __init__(self, number, range) -> None:
        self.number = number
        self.range = range      
        
        assert range >= 0, f"n:{number} r:{range}" 

    def __str__(self) -> str:
        return f"n:{self.number} r:{self.range}"
    
    def __repr__(self) -> str:
        return str(self)

class mapper:
    def __init__(self, destination, source, range) -> None:
        self.destination = destination
        self.source = source
        self.range = range
        self.offset = destination - source
        
    def __str__(self) -> str:
        return f"s:{self.source} d:{self.destination} r:{self.range} o:{self.offset}"
        
    def __repr__(self) -> str:
        return str(self)
        

seeds = data[0].split(": ")[1].split(" ")
seeds = list(map(int, seeds))

newseeds:list[seed] = []

for i in range(0, len(seeds), 2):
    newseeds.append(seed(seeds[i], seeds[i+1]))

seeds = newseeds

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
    

for map in maps:
    maps[map] = sorted(maps[map], key=lambda x: x.source)
    
    maps[map].append(mapper(999999, 99999999, 9999999))

# for i in maps:
#     print(maps[i])

# print(seeds)
# print(maps)    

# seeds = [seeds[0]]
print("seeds:", seeds)
print()

results = []

for s in seeds:
    
    # print("seed:", seed)
    
    seedshards:list[seed] = [s]
    newshards:list[seed] = []
    
    for map in maps:
        
        print("map:", map)
        print("SS:", seedshards)
                
        for shard in seedshards:
            
            shard_base = shard.number
            shardchange = len(newshards)
        
            # this assumes that maps are sorted
            for mapi, entry in enumerate(maps[map]):
                print("shard:", shard)
                print("entry:", entry)
                
                # if entry is not relevant than copy it over with no modifications
                if shard.number + shard.range < entry.source:
                    print("not relevant")
                    newshards.append(seed(shard_base, shard.range))
                    break
                
                # if entry is smaller than shard, keep on going
                if entry.source + entry.range < shard.number:
                    print("map is too small")
                    continue
                
                # if map completely covers shard
                if entry.source <= shard.number and entry.source + entry.range >= shard.number + shard.range:
                    print("map completely covers shard")
                    new_source = entry.source
                    new_range = entry.range
                    if shard.number > entry.source:
                        new_source = shard.number
                        new_range = (entry.source + entry.range) - new_source
                    
                    
                    m_range = min(shard.range, new_range)
                    newshards.append(seed(shard.number + entry.offset, m_range))
                    
                    break
                    
                
                # if shard intersects with map, but doesn't cover
                if shard.number + shard.range >= entry.source and shard.number + shard.range < entry.source + entry.range:
                    print("non-covering map intersection")
                    
                    new_source = entry.source
                    new_range = entry.range
                    if shard.number > entry.source:
                        new_source = shard.number
                        new_range = (entry.source + entry.range) - new_source
                        
                                    
                    if new_source == shard.number:
                        m_range = min(shard.range, new_range)
                        newshards.append(seed(entry.destination, m_range))
                        
                        if shard.range > new_range:
                            newshards.append(seed(shard.number+m_range, shard.range - m_range))
                    
                    if shard.number < entry.source:
                        
                        # if shard is below entry, put in the range that isn't modified
                        unmodified = entry.source - shard.number
                        newshards.append(seed(shard.number, unmodified))
                        
                        # create moved range shard
                        ran = shard.range - unmodified
                        newshards.append(seed(entry.source, ran)) 
                    
                    print("ns:", newshards)
                    break
                        
                if entry.source + entry.range > shard.number and entry.source+entry.range <= shard.number + shard.range:
                    print("partial cover shar[map]")
                    new_source = entry.source
                    new_range = entry.range
                    if shard.number > entry.source:
                        new_source = shard.number
                        new_range = (entry.source + entry.range) - new_source
                        
                    newshards.append(seed(new_source, new_range))
                    
                    leftoverrange = (shard.number+shard.range) -  (entry.source+entry.range)
                    
                    shard.number = entry.source + entry.range
                    shard.range = leftoverrange
                    
                    assert shard.number >= 0, shard.number
                    assert shard.range >= 0, shard.range
                    
                    continue
                    
                # if shard covers map
                # must generate three ranges
                if shard.number + shard.range > entry.source and shard.number + shard.range > entry.source + entry.range:
                    print("map covered by shard")
                    
                    # modified digits of range that is in between
                    newshards.append(seed(entry.destination, entry.range))
                    
                    # continue to check further entries
                    # set shard number and range to end of entry source
                    leftoverrange = (shard.number+shard.range) -  (entry.source+entry.range)
                    
                    shard.number = entry.source + entry.range
                    shard.range = leftoverrange
                    
                    assert shard.number >= 0, shard.number
                    assert shard.range >= 0, shard.range
                                    
            if len(newshards) == shardchange:
                print("NONCHANGE in newshard found")
                newshards.append(shard)
                
        #print(newshards)
        if len(newshards) == 0:
            print("EMPTY NEWSHARDS FOUND")
            newshards = seedshards
            
        print("newshards:", newshards)
        input()
            
        seedshards = newshards
        newshards = []
        
        print("SS", seedshards)

    
    
    
    
    lowest = seedshards[0].number
    for s2 in seedshards:
        if s2.number < lowest:
            lowest = s2.number
            
    print(lowest)
    results.append(lowest)



print("RESULTS")
for i in results:
    print(i)