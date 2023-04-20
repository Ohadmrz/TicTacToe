booth_list = []
board = int(input("board's size: "))
for b in range(1, board + 1):
    booth_list.append(b)
space_no_end = "+~~~~~"
space_end = "+"
space = (f"{(space_no_end)*board}{space_end}")
print(f" {space}")
for i in booth_list[0:(len(booth_list)*len(booth_list)):len(booth_list)]:
    for z in booth_list[0:(len(booth_list)+1):]:
        booth = i+z
        kir = "|"
        kirstart = (f" {kir}  {booth}")
        kirot1 = (f"  {booth}  ")
        kirot2 = (f" {booth}  ")
        kirot3 = (f" {booth} ")
        if booth < 100:
            if booth < 10:
                if booth == 1:
                    print(kirstart,end="  |")
                else: print(kirot1,end="|")
            else: print(kirot2,end="|")
        else: print(kirot3, end="|")
    print('\n',space,'\n',end=" |")

#print("||||||> i'm happy to present you: ~THE BOARD~  (angle's singing uuuuhhh) <||||||")
print(booth_list)


#akol beseder:

def board_build():
    booth_list = []
    board = int(input("board's size: "))
    space_no_end = "+~~~~~"
    space_end = "+"
    space = (f"{(space_no_end)*board}{space_end}")
    print(f" {space}")
    for i in range(0,(board*board),board):
        for j in range(1,board+1):
            booth = (j + i)
            kir = "|"
            kirstart = (f" {kir}  {booth}")
            kirot1 = (f"  {booth}  ")
            kirot2 = (f" {booth}  ")
            kirot3 = (f" {booth} ")
            if booth < 100:
                if booth < 10:
                    if booth == 1:
                        print(kirstart,end="  |")
                    else: print(kirot1,end="|")
                else: print(kirot2,end="|")
            else: print(kirot3, end="|")
        print('\n',space,'\n',end=" |")
    for b in range(1,board+1):
        booth_list.append(b)
    print("'m happy to present you: ~THE BOARD~  (angle's singing uuuuhhh)")
    player_names()