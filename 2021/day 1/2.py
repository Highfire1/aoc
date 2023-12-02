with open("day 1/in.txt", "r") as measurements:
    
    # convert string to int
    m = []
    for x in measurements.readlines():
        m.append(int(x))

    i = 3
    prevwindow = m[0] + m[1] + m[2]
    count = 0

    # iterate through every measurement
    while i < len(m) - 2:
        window = m[i] + m[i+1] + m[i+2]
        
        if window > prevwindow:
            count += 1

        prevwindow = window
        i += 1

print(count)