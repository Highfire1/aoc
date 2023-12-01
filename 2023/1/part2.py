
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
    
    for i in range(len(line)-1):
                    
        for n in numbers:
            num_ascii = n[0]
            num_len = len(num_ascii)
            
            matching = line[i : i + num_len] == num_ascii
                        
            if matching:
                line = line[0:i] + n[1] + line[i+1:]
                                     
    return line


with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 

sum = 0

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

    sum += int(firstdigit + lastdigit)
        
print(sum)
