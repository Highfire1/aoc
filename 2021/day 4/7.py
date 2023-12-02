# generate board
with open("day 4/in.txt", "r") as infile:
    bingo = infile.readline().splitlines()
    bingo = bingo[0].split(",")

    boards = []

    for j in range(100): # 100
        tempboard = []
        infile.readline()

        for i in range(5):
            line = infile.readline().split()
            tempboard.append(line)
        
        boards.append(tempboard)

for number in bingo:
    for boardi, board in enumerate(boards):
        for linei, line in enumerate(board):
            if str(number) in line:
                index = line.index(str(number))
                boards[boardi][linei][index] = -1

                cb = boards[boardi]
                print(cb)

                for l in cb:
                    if l == [-1]*5:
                        print("MATCH")
                        print("final num", number)
                        print("line #", (boardi*6)+3)
                        exit()
                
                if  set([cb[0][0], cb[1][1], cb[2][2], cb[3][3], cb[4][4]]) == {-1} or \
                    set([cb[4][0], cb[3][1], cb[2][2], cb[1][3], cb[0][4]]) == {-1}:
                    print("MATCH")
                    print("final num", number)
                    print("line #", (boardi*6)+3)
                    exit()
                
                if set([cb[0][linei], cb[1][linei], cb[2][linei], cb[3][linei], cb[4][linei]]) == {-1}:
                    print("MATCH")
                    print("final num", number)
                    print("line #", (boardi*6)+3)
                    exit()
         



print(boards)
                
