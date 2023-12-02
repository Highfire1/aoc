distance = 0
altitude = 0

with open("day 2/in.txt", "r") as measurements:
    for instruction in measurements.readlines():
        direction, amount = instruction.split()
        amount = int(amount)
        if direction == "forward":
            distance += amount
        elif direction == "up":
            altitude -= amount
        elif direction == "down":
            altitude += amount

print(distance, altitude)
print("final:", distance*altitude)