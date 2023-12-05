with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 


cards = [1] * len(data)


for i, line in enumerate(data):
            
    ss = line.split(": ")
    nums = ss[1].split(" | ")
    
    winners = [x for x in nums[0].split() if x.strip()]
    ours = [x for x in nums[1].split() if x.strip()]

    gamewins = 0
    for n in ours:
        if n in winners:        
            gamewins += 1
    
    for n in range(gamewins):
        cards[i + n + 1] += cards[i]    


print(sum(cards))