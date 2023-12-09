import math


with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 
    
sum = 0

class play:
    def __init__(self, hand, bid, score=None) -> None:
        self.hand:str = hand
        self.bid:int = int(bid)
        self.score:int = score
        self.type = None
    
    def __str__(self) -> str:
        return f"{self.hand} {self.bid} {self.score} {self.type}"
    
    def __repr__(self) -> str:
        return str(self)
    
    
plays:list[play] = []

for line in data:
    s = line.split(" ")
    plays.append(play(s[0], s[1]))
    

#print(plays)

score = "23456789TJQKA"
score = [*score]

def numscore(hand):
    s = 0
    for c in hand:
        s += 1 + score.index(c)
    
    return s

scores = []

for p in plays:
    
    split = [*p.hand]
    print(split)
    
    cleaned_hand = sorted(split, key=lambda x: score.index(x))
    
    uniques = []
    longest = ["", 0, 1]
    pairs = 0
    
    
    for card in cleaned_hand:
        
        print(card, longest)
        
        if longest[0] == card:
            longest[1] += 1
        else:
            if longest[1] == 2:
                pairs += 1
                
            longest[0] = card
            longest[2] = max(longest[1], longest[2])
            longest[1] = 1
        
        if card not in uniques:
            uniques.append(card)
    
    longest[2] = max(longest[1], longest[2])
    print("# uniques:", len(uniques))
    print("longest chain:", longest[2])
    
    out = 0
    
    if longest[2] == 5:
        out += 13 * 10000 ** 7
        p.type = "five of a kind"
        
    if longest[2] == 4:
        out += 13 * 10000 ** 6
        p.type = "four of a kind"
        
    elif longest[2] == 3 and len(uniques) == 2:
        out += 13 * 10000 ** 5
        p.type = "full house"
        
    elif longest[2] == 3:
        out += 13 * 10000 ** 4
        p.type = "three of a kind"
        assert len(uniques) == 3
        
    elif len(uniques) == 3:
        out += 13 * 10000 ** 3
        p.type = "two pairs"
        
    elif longest[2] == 2:
        out += 13 * 10000 ** 2
        p.type = "one pair"
    
    elif p.type == None:
        out += 13 * 10000 ** 1
        p.type = "high card"
    
    
    out += (score.index(p.hand[0])+1) * (13 ** 5)
    out += (score.index(p.hand[1])+1) * (13 ** 4) 
    out += (score.index(p.hand[2])+1) * (13 ** 3) 
    out += (score.index(p.hand[3])+1) * (13 ** 2)
    out += (score.index(p.hand[4])+1) * (13 ** 1)
        
    p.score = out
        
    # p.score = 

final = sorted(plays, key=lambda x: x.score)

final_out = 0

print()
print("FINAL:")

for i, hand in enumerate(final):
    print(f"{hand.bid} * {i+1}", "\t", hand)
    final_out += hand.bid * (i+1)
    # print(final_out)

print("OUT:")
print(final_out)