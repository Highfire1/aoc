count = 0

with open("day 1/in.txt", "r") as measurements:
    previtem = measurements.readline()

    for item in measurements.readlines():
        if item > previtem:
            count += 1
        previtem = item

print(count + 1) # off by one, not sure why ;-;