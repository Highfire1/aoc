with open("day 7/in.txt", "r") as infile:
    data = infile.read().split(",") # read to list
    data = list(map(int, data)) # convert to int


lowest = 1000000000

for i in range(max(data)):
    fuelspent = 0
    for item in data:
        fuelspent += abs(i - item) 
    
    if fuelspent < lowest:
        print(f"New lowest of {fuelspent} at {i}.")
        lowest = fuelspent