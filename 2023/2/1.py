with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 

sum = 0

for line in data:
    
    split = line.split(": ")
    number = int(split[0].split(" ")[1])
    
    sets = split[1].split("; ")
    
    cubes = {
        "red" : 0,
        "green" : 0,
        "blue" : 0,
    }
    
    for reveals in sets:
        
        plays:list[str] = reveals.split(", ")
        
        for play in plays:
            
            split = play.split(" ")
            num = int(split[0])
            color = split[1]
                        
            if color in cubes:
                cubes[color] = max(cubes[color], num)
            else:
                cubes[color] = num
    
    if cubes["red"] <= 12 and cubes["green"] <= 13 and cubes["blue"] <= 14:
        sum += number
        
print(sum)
    
        
        
        

    
    