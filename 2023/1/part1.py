with open("input.txt", "r") as fi:
    data = fi.readlines()
    
sum = 0

for line in data:

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