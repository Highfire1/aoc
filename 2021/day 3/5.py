#incredibly messy and inefficient but good enough lol

gamma = [0]*12
epsilon = [0]*12

# count data from file
with open("day 3/in.txt", "r") as infile:
    for line in infile.readlines():

        for i, char in enumerate(line):
            if char.isspace():
                continue
            if char == "0":
                gamma[i] += 1
            else:
                epsilon[i] += 1
        line = int(line)

# convert into gamma/epsilon
ga = [0]*12
ep = [0]*12

for i in range(12):
    if gamma[i] > epsilon[i]:
        ga[i] = "1"
        ep[i] = "0"
    else:
        ga[i] = "0"
        ep[i] = "1"
    
ga = "".join(ga)
ep = "".join(ep) 

# convert into decimal
print(int(ga, 2) * int(ep, 2))