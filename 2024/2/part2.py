

data:list[list] = []

with open("input.txt", "r") as fi:
    for line in fi.readlines():
        l = line.split(" ")
        data.append([int(x) for x in l])

def determine_safe(arr:list) -> bool:
    state = 0
    last = arr[0]
    
    for point in arr[1:]:
        difference = point - last
        
        if abs(difference) < 1 or abs(difference) > 3:
            return False
        
        if point > last:
            if state == 2:
                return False
            state = 1
        elif point < last:
            if state == 1:
                return False
            state = 2
        
        last = point
    
    return True
   
    
import copy


safe_report_count = 0

for report in data:
    
    # print(report)
    
    safe = False
    if determine_safe(report):
        safe = True
    
    for i in range(len(report)+1):
        temp = copy.deepcopy(report)
        # print(i, len(report))
        if i != len(report):
            temp.pop(i)
            
        test = determine_safe(temp)
        # print(temp, test)
        
        if test:
            safe = True
            break
            
    
    # input(safe)
    
    if safe:
        safe_report_count+=1

print(safe_report_count)