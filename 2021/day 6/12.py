with open("day 6/in.txt", "r") as infile:
    data = infile.read().split(",")
    data = list(map(int, data))


fish = [0] * 9 # 0 to 8

# parse entry data
for f in data:
    fish[f] += 1

# business logic
for day in range(256):
    newfish = fish[1:9]
    newfish[6] += fish[0]   
    newfish.append(fish[0])
    
    fish = newfish.copy()

print(sum(fish))