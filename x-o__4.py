# rows = int(input("Num: "))
# for i in range(rows+1,0,-1):
#     for j in range(rows+1-i,0,-1):
#         print(j, end=" ")
#     print('\n',end="")

booth_list = []
amuda_X = []
amuda_O = []
shura_X = []
shura_O = []
board = int(input("board's size: "))
for b in range(1, (board * board) + 1):
    booth_list.append(b)
for h in range(1, board + 1):
    amuda_X.append(0)
    amuda_O.append(0)
    shura_X.append(0)
    shura_O.append(0)


def tavla():
    space_no_end = "+~~~~~"
    space_end = "+"
    space = (f"{(space_no_end) * board}{space_end}")
    print(f" {space}")
    for i in range(0, (board * board), board):
        for j in range(1, board + 1):
            booth = booth_list[((i + j) - 1)]
            kir = "|"
            kirstart = (f" {kir}  {booth}")
            kirot1 = (f"  {booth}  ")
            kirot2 = (f" {booth}  ")
            kirot3 = (f" {booth} ")
            if type(booth) is int:
                if booth < 100:
                    if booth < 10:
                        if booth == 1:
                            print(kirstart, end="  |")
                        else:
                            print(kirot1, end="|")
                    else:
                        print(kirot2, end="|")
                else:
                    print(kirot3, end="|")
            elif i == 0 and j == 1 and booth_list[0] == "X" or booth_list[0] == "O":
                print(kirstart, end="  |")
            else:
                print(kirot1, end="|")
        print('\n', space, '\n', end=" |")


tavla()
print(booth_list)
a = 1
booth_list[a - 1] = 'X'
a = 5
booth_list[a - 1] = 'X'
a = 9
booth_list[a - 1] = 'X'
a = 13
booth_list[a - 1] = 'X'
# a= 31
# booth_list[a-1]= 'X'
# a= 37
# booth_list[a-1]= 'X'
# a= 43
# booth_list[a-1]= 'X'
tavla()
print(booth_list)

alachson_from_northwest_X = 0
alachson_from_northwest_O = 0
alachson_from_northeast_X = 0
alachson_from_northeast_O = 0

i = 0
while i < board:
    if booth_list[((board * i) + i)] == "X":
        alachson_from_northwest_X += 1
    elif booth_list[((board * i) + i)] == "O":
        alachson_from_northwest_O += 1
    i += 1
if alachson_from_northwest_X == board or alachson_from_northwest_O == board:
    print("you win0")

s = 0
while s <= board:
    if booth_list[((board * s) - s)] == "X":
        alachson_from_northeast_X += 1
    elif booth_list[((board * s) - s)] == "O":
        alachson_from_northeast_O += 1
    s += 1
if alachson_from_northeast_X == board or alachson_from_northeast_O == board:
    print("you win1")
    # if (board)

# print("'m happy to present you: ~THE BOARD~  (angle's singing uuuuhhh)")

for amuda, val in enumerate(amuda_X):
     c = -1
     while c < (board-1):
         if booth_list[((board * c) + board)] == "X":
             amuda_X[c+1] += 1
         #elif booth_list[((board * c) + board)] == "O":
#             #amuda_1_O += 1
         c += 1
     if val == board:
         print("you win2")
             #or amuda_O[] == board:
print(amuda_X)
