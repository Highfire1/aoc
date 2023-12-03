with open("input.txt", "r") as fi:
    data = fi.read().splitlines() 

#print(data)


max_i = len(data)

sum = 0

def selectnumbers(row_index, char_index) -> int:
    
    if row_index < 0 or row_index >= len(data):
        return 0
    
    if char_index < 0 or char_index > len(data[0]):
        return 0
    
    
    selected = ""
    
    
    for i, char in enumerate(data[row_index]):
        
        #print(i, char)
        if char.isdecimal():
            selected += char
            
        else:
            if i == char_index:
                selected = ""
                break
            
            if i >= char_index:
                break
        
            selected = ""
        
            
        
            
    
    if selected.isspace() or selected == "":
        return 0
            
    front = data[row_index][0: i - len(selected)]
    back = data[row_index][i:]
    
    assert len(data[row_index]) == len(front + "."*len(selected) + back)
    data[row_index] = front + "."*len(selected) + back
    
    if False:
        print(front, back)
        print(row_index, char_index, data)
        print(selected)
        print() 
    
        print(selected)
    return int(selected)


for i, line in enumerate(data):
    
    for j, symbol in enumerate(line):
        
        if symbol != "." and not symbol.isnumeric():
            
            sum += selectnumbers(i-1, j-1)
            sum += selectnumbers(i-1, j)
            sum += selectnumbers(i-1, j+1)
            
            sum += selectnumbers(i, j-1)
            sum += selectnumbers(i, j+1)
            
            sum += selectnumbers(i+1, j-1)
            sum += selectnumbers(i+1, j)
            sum += selectnumbers(i+1, j+1)
            
    #print()
        
print(sum)