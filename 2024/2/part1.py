

data = []

with open("input.txt", "r") as fi:
    for line in fi.readlines():
        l = line.split(" ")
        data.append([int(x) for x in l])

    

safe_reports = 0

for report in data:
    state = 0
    last = report[0]
    safe = True
    
    for point in report[1:]:
        difference = point - last
        
        if abs(difference) < 1 or abs(difference) > 3:
            safe = False
        
        if point > last:
            if state == 2:
                safe = False
            state = 1
        elif point < last:
            if state == 1:
                safe = False
            state = 2
        elif point == last:
            safe = False
        
        last = point
    
    if safe:
        safe_reports+= 1
        
print(safe_reports)

