distance = 0
altitude = 0
aim = 0

with open("day 2/in.txt", "r") as measurements:
    for instruction in measurements.readlines():
        direction, amount = instruction.split()
        amount = int(amount)

        if direction == "forward":
            distance += amount
            altitude += aim * amount

        elif direction == "up":
            aim -= amount

        elif direction == "down":
            aim += amount

print(distance, altitude)
print("final:", distance*altitude)