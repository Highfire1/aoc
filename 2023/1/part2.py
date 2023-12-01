
def cleaner(line:str) -> str:
    
    numbers = [
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9")
    ]
    
    i = 0
    
    while i < len(line)-1:
                    
        for n in numbers:
            num_ascii = n[0]
            num_len = len(num_ascii)
            
            within_bounds = i + num_len-1-1 <= len(line)-1
            matching = line[i : i + num_len] == num_ascii
            
            #print(line[i : i + num_len], n, within_bounds, matching)
            
            if within_bounds and matching:
                
                line = line[0:i] + n[1] + line[i+1:]
                
                i+= len(n[1]) -2
                print(line)
                
        i+=1
                     
    return line


with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 

sum = 0

i = 0
for line in data:
    
    line = cleaner(line)
    
    
    for char in line:
        if char.isdecimal():
            firstdigit = char
            break
        
    for char in reversed(line):
        if char.isdecimal():
            lastdigit = char
            break

    add = int(firstdigit + lastdigit)
    sum += add
    
    print(line)
    print(add)
    
    #input()
    i+=1
        
print(sum)
print(i)