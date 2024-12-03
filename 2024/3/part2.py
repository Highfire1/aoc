

data = ""

with open("input.txt", "r") as fi:
    for line in fi.readlines():
        data += line
      


def extract_functions(s: str) -> list[str]:
    funcs = []
    
    saving_function = False
    function = ""
        
    for i in range(len(data)):
                    
        if data[i:i+4] == "mul(":
            saving_function = True
            function = ""
        
        if data[i:i+3] == "do(":
            saving_function = True
            function = ""
        
        if data[i:i+6] == "don't(":
            saving_function = True
            function = ""
        
        if saving_function:
            function += data[i]
                        
        if data[i] == ")" and saving_function:
            # print(f"{in_func_text}\t\t{data[i-len(in_func_text)-5:i+5]}")
            funcs.append(function)
            saving_function = False
            function = ""
                    
    return funcs





f = extract_functions(data)
# print(f)

result = 0
do = True

for func in f:
    func_data = func.split("(", 1) # i spent 30 minutes debugging this
    func_data = func_data[1][0:-1]
    
    if func == "do()":
        do = True
    
    elif func.startswith("mul"):
        if not do:
            pass
        
        elif "," not in func_data:
            pass
            
        else:
            split = func_data.split(",")
            
            if len(split) != 2 or not split[0].isdigit() or not split[1].isdigit():
                print("FAIL TO PARSE2", func)
                pass
            # elif len(split[0]) > 3 or len(split[1]) > 3:
            #     print("FAIL TO PARSE3", func)
            else:
                if do:
                    result += (int(split[0]) * int(split[1]))
                # print(result, int(split[0]) * int(split[1]))
    
    elif func == "don't()":
        do = False
    
    else:
        # doesn't trip
        print("unrecognized??", func)
        input()
    
      
print()  
print(result)