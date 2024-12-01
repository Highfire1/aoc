

list_1:list[int] = []
list_2:list[int] = []

with open("input.txt", "r") as fi:
    
    for line in fi.readlines():
        data = line.split("   ")
        list_1.append(int(data[0]))
        list_2.append(int(data[1]))


list_1.sort()
list_2.sort()


similarity_score = 0

for i in list_1:
    similarity_score += i * list_2.count(i)

print(similarity_score)