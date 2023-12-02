with open("day 7/in.txt", "r") as infile:
    data = infile.read().split(",") # read to list
    data = list(map(int, data)) # convert all to int


lowest = 1000000000

for i in range(max(data)):
    fuelspent = 0
    for item in data:
        for dist in range(abs(i - item)):
            fuelspent += dist + 1
    
    if fuelspent < lowest:
        print(f"New lowest of {fuelspent} at {i}.")
        lowest = fuelspent