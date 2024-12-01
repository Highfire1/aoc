

list_1:list[int] = []
list_2:list[int] = []

with open("input.txt", "r") as fi:
    
    for line in fi.readlines():
        data = line.split("   ")
        list_1.append(int(data[0]))
        list_2.append(int(data[1]))


list_1.sort()
list_2.sort()

assert(len(list_1) == len(list_2))

difference = 0

for i1, i2 in zip(list_1, list_2):
    diff = abs(i1 - i2)
    assert diff >= 0
    difference += diff
  
print(difference)
# print(list_1)