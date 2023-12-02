with open("day 9/in.txt", "r") as infile:
    data = infile.read().split() # read to list
count = 0

for rnum, row in enumerate(data):
    for mnum, measurement in enumerate(row):
        mea = int(measurement)

        up = 100
        down = 100
        right = 100
        left = 100

        if rnum - 1 >= 0:
            up = int(data[rnum - 1][mnum])

        if rnum + 1 < len(data):
            down = int(data[rnum + 1][mnum])

        if mnum + 1 < len(row):
            right = int(row[mnum + 1])

        if mnum - 1 >= 0:
            left = int(row[mnum - 1])
        
        if mea < up and mea < down and mea < right and mea < left:
            count += (1 + mea)
            print(mea, "|", up, down, right, left)
        
print(count)

# 547 too low
# 593 too high
# 631 too high