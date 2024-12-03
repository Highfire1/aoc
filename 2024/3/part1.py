

data = ""

with open("input.txt", "r") as fi:
    for line in fi.readlines():
        data += line
      

found = ""  

in_mul = False
skip = 0
in_mul_text = ""

result = 0
# print(data)
        
for i in range(len(data)-1):
    
    if skip > 0:
        skip -= 1
        continue
    
    if in_mul:
        in_mul_text += data[i]
    
    if data[i] == ")" and in_mul:
        in_mul_text = in_mul_text[0:-1]
        
        if "," not in in_mul_text:
            in_mul = False
            in_mul_text = ""
        else:
            
            
            split = in_mul_text.split(",")
            
            if len(split) != 2 or not split[0].isdigit() or not split[1].isdigit():
                in_mul = False
                in_mul_text = ""
            else:
                # print(f"parsing mul({in_mul_text}) = {int(split[0]) * int(split[1])}")
                
                
                print(data[i-len(in_mul_text)-4:i+1])
                
                # print(f"adding {int(split[0]) * int(split[1])}")
                result += int(split[0]) * int(split[1])
                in_mul = False
                in_mul_text = ""
        
        continue
                
            
            
        
    # input(data[i:i+3])
    
    if data[i:i+4] == "mul(":
        in_mul = True
        skip += 3
        in_mul_text = ""
        
print(result)
