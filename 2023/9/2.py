import math
import sys

with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 
  

cleaned_data = []

for line in data:
    
    vals = list(map(int, line.split(" ")))
    cleaned_data.append(vals)
    

all_histories:list[list[list[int]]] = []

for line in cleaned_data:
    
    histories = [line]
    
    while True:
        
        new_history = []
        
        last = histories[-1][0]
                
        for time in histories[-1][1:]:
            
            difference = time - last
            new_history.append(difference)
            last = time
            
        histories.append(new_history)
            
        if new_history.count(0) == len(new_history):
            break
        
    all_histories.append(histories)

sum = 0

for line in all_histories:
    
    substract = 0
    # add = 0
    
    for difference in reversed(line):
        
        print(substract, difference)
        
        substract = difference[0] - substract
        
        print(substract)
    
    # print("final", substract)
    # print(add)
    sum += substract

    
    print()
    

print("SUM:")
print(sum)