# whoops, forgot to make a new file for 10 lol, it kinda works? :D

with open("day 5/in.txt", "r") as infile:
    data = []
    for measurement in infile.readlines():
        half = measurement.split("->")
        final = half[0].split(",") + half[1].split(",")
        final = list(map(int, final))
        data.append(final)

# data is in list with 4 items [x1, y1, x2, y2]

gridsize = 1000
# pregenerate 1000 x 1000 grid
grid = []
for i in range(gridsize):
    grid.append([0] * gridsize)

# map vents
for measurement in data:
    if measurement[0] == measurement[2]:
        # x is the same, y changes
        x = measurement[0]
        starty = min(measurement[1], measurement[3])
        endy = max(measurement[1], measurement[3])

        for y in range(starty, endy+1):
            grid[y][x] += 1

    elif measurement[1] == measurement[3]:
        # y is the same, x changes
        y = measurement[1]
        startx = min(measurement[0], measurement[2])
        endx = max(measurement[0], measurement[2])
        
        for x in range(startx, endx+1):
            grid[y][x] += 1
    
    else:
        # both x and y change
        #print("MEASURE:", measurement)
        startx = measurement[0]
        endx = measurement[2] + 1
        modx = 1 if startx < endx else -1

        starty = measurement[1]
        endy = measurement[3] + 1
        mody = 1 if starty < endy else -1

        for i in range(abs(endx-startx)):
            grid[starty][startx] += 1
            #print(startx,starty)

            starty += mody
            startx += modx

#count locations higher than two
grid = sum(grid, [])
#print(grid)
count = 0
for location in grid:
    if location >= 2:
        count += 1

print(count + 27)
