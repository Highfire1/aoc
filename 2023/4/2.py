with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 


cards = [1] * len(data)


for i, line in enumerate(data):
            
    ss = line.split(": ")
    nums = ss[1].split(" | ")
    
    winners = nums[0].split(" ")
    ours = nums[1].split(" ")
    
    winners = list(filter(None, winners))
    ours = list(filter(None, ours))

    gamewins = 0
    for n in ours:
        if n in winners:        
            gamewins += 1
    
    for n in range(gamewins):
        cards[i + n + 1] += cards[i]    


sum = 0
for i in cards:
    sum += i
print(sum)