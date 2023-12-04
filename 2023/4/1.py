with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 
    
cards = []
sum = 0

for line in data:
    
    winnings = 0
    
    ss = line.split(": ")
    
    nums = ss[1].split(" | ")
    
    winners = nums[0].split(" ")
    ours = nums[1].split(" ")
    
    winners2 = []
    for i, w in enumerate(winners):
        if w != "":
            winners2.append(int(w))
        
    print(ours)
    ours2 = []
    for i, o in enumerate(ours):
        if o != "":
            ours2.append(int(o))
    
    for n in ours2:
            
        if n in winners2:
            if winnings == 0:
                winnings = 1
            else:
                winnings *= 2
    
        
    print(winnings)
    print()
    sum += winnings
    
print(sum)
