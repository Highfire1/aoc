with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 
    
cards = []
sum = 0

winnings = []
for i in range(len(data)):
    winnings.append(0)

for II, line in enumerate(data):
    
    winnings[II] = winnings[II] + 1
        
    ss = line.split(": ")
    
    nums = ss[1].split(" | ")
    
    winners = nums[0].split(" ")
    ours = nums[1].split(" ")
    
    winners2 = []
    for i, w in enumerate(winners):
        if w != "":
            winners2.append(int(w))
        
    #print(ours)
    ours2 = []
    for i, o in enumerate(ours):
        if o != "":
            ours2.append(int(o))
    
    gamewins = 0
    
    for n in ours2:
            
        if n in winners2:
            gamewins += 1
    
    for n in range(gamewins):
        winnings[II + n + 1] += 1 * winnings[II]
        
    #print(winnings)
    

for i in winnings:
    sum += i
print(sum)

#print(winnings)