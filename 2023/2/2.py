with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 

sum = 0

for game in data:
    
    split = game.split(": ")
    number = int(split[0].split(" ")[1])
    
    sets = split[1].split("; ")
    
    cubes = {
        "red" : 0,
        "green" : 0,
        "blue" : 0,
    }
    
    for reveals in sets:
        
        plays = reveals.split(", ")
        
        for play in plays:
            
            split = play.split(" ")
            num = int(split[0])
            color = split[1]
                        
            cubes[color] = max(cubes[color], num)
    
    mult = 1
    for i in cubes:
        mult *= cubes[i]        
    sum += mult 
        
print(sum)
    
        
        
        

    
    