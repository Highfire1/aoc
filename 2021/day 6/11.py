with open("day 6/in.txt", "r") as infile:
    data = infile.read().split(",")
    data = list(map(int, data))

for day in range(80):
    newfish = 0
    for i, fish in enumerate(data):

        if fish == 0:
            data[i] = 6
            newfish += 1
        else:
            data[i] -= 1

    for fish in range(newfish):
        data.append(8)

print(len(data))