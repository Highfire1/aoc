# accepted modes: most_common & least_common
def findbit(mode):

    with open("day 3/in.txt", "r") as infile:
        data = infile.read().splitlines()

    for digit in range(12):

        # read bit for each digit on each line
        count = 0
        for i, line in enumerate(data):

            if line == 0:
                continue

            if line[digit] == "0":
                count -= 1
            else:
                count += 1
        
        # determine removal bit
        # probably can be optimized but my brain already hates this
        if count == 0:
            if mode == "most_common":
                remove = "1"
            else:
                remove = "0"

        elif mode == "most_common":
            if count > 0:
                remove = "1"
            else:
                remove = "0"

        elif mode == "least_common":
            if count > 0:
                remove = "0"
            else:
                remove = "1"

        # "remove" bad entries from data
        validcount = 0
        for i, line in enumerate(data):
            if line == 0:
                continue
            if line[digit] == remove:
                data[i] = 0
            else:
                validcount += 1
                final = line
        
        if validcount == 1:
            return final

oxygen = findbit("most_common")
carbon = findbit("least_common")

print(oxygen, carbon)
oxygen = int(oxygen, 2)
carbon = int(carbon, 2)

print(oxygen*carbon)