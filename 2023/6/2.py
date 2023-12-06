with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 
    
sum = 0


time = data[0].split(":")

time[1] = time[1].replace(" ", "")
time = [x for x in time[1].split() if x.strip()]



distance = data[1].split(":")
distance[1] = distance[1].replace(" ", "")
distance = [x for x in distance[1].split() if x.strip()]

distance = list(map(int, distance))
time = list(map(int, time))

print(time)
print(distance)

results = 1

for i in range(len(time)):
    
    button_held = 0
    
    succeeds = 0
    
    for time_held in range(time[i]):
        
        remaining_time = time[i] - time_held
        
        travel = time_held * remaining_time
        
        
        # print()
        
        if travel > distance[i]:
            # print("match")
            # print(time_held, remaining_time, travel)
            succeeds += 1
    
    
    # print(succeeds)
    # input()
    results *= succeeds
    

print(results)