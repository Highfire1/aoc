### WARNING : DOES NOT WORK AT ALL LIKE GOD

def printboard(board):
    print("==================")
    for l in board:
        for item in l:
            if item == -1:
                print("   ", end="")
            else:
                print(str(item).rjust(3), end='')
        print("")
    print("==================")

def countnonemptylists(list_):
    count = 0
    for x in list_:
        if x != []:
            count += 1
    return count

# generate board
with open("day 4/in.txt", "r") as infile:
    bingo = infile.readline().splitlines()
    bingo = bingo[0].split(",")

    boards = []

    for j in range(100): # file is 600 lines long, each board is 6 lines long, therefore 100 boards
        tempboard = []
        infile.readline()

        for i in range(5):
            line = infile.readline().split()
            tempboard.append(line)
        
        boards.append(tempboard)


# eliminate bad boards
eliminatedcount = 0

for number in bingo:
    for boardi, board in enumerate(boards):
        for linei, line in enumerate(board):
            if str(number) in line:
                index = line.index(str(number))
                boards[boardi][linei][index] = -1

                cb = boards[boardi]

                # vertical
                # horizontal
                # diagonal1
                # diagonal2
                if  set([cb[0][index], cb[1][index], cb[2][index], cb[3][index], cb[4][index]]) == {-1} or \
                    set([cb[linei][0], cb[linei][1], cb[linei][2], cb[linei][3], cb[linei][4]]) == {-1} or \
                    set([cb[0][0], cb[1][1], cb[2][2], cb[3][3], cb[4][4]]) == {-1} or \
                    set([cb[4][0], cb[3][1], cb[2][2], cb[1][3], cb[0][4]]) == {-1}:
                    
                    # print("MATCH")
                    # printboard(cb)
                    # print(cb)
                    # print("line", linei, "index", index)
                    # print("final num", number)
                    # print("line #", (boardi*6)+3)
                    boards[boardi] = []
                    eliminatedcount += 1
                    print(countnonemptylists(boards), eliminatedcount)
    if eliminatedcount > 90: # for some reason only like 91 boards get solved ;-;
        break

print(boards)