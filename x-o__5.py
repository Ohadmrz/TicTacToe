# goods = [['apple', 'pear', 'peach', 'chery' ],
# ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
#     'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry' ]]
#
# longest_words = [goods[0][0]]
# longest_indexes = [[0, 0]]
#
# for index, goods_list in enumerate(goods):
#     for inner_index, good in enumerate(goods_list):
#         good_len = len(good)
#         longest_len = len(longest_words[-1])
#
#         if good_len > longest_len:
#             longest_words.clear()
#             longest_indexes.clear()
#
#             longest_words.append(good)
#             longest_indexes.append([index, inner_index])
#
#         elif good_len == longest_len:
#             longest_words.append(good)
#             longest_indexes.append([index, inner_index])
#
# for index, word in enumerate(longest_words):
#     print(f"{word} - (index: {longest_indexes[index][0]}, inner index: {longest_indexes[index][1]})")
booth_list = []
commands = ("play","quit")

def playorquit():
    while True:
        command = input("write 'play' to..play\nor 'quit' to break my heart: \n")
        if command not in commands:
            print("what?")
        else:
            return command

# def player_names(n1,n2) -> str:
#     print("now just write down your Names cause that's super important of course..")
#     print(playersnames)
#     tools()
players_tools = []
def tools():
    #players_tools = []
    change_tools = ("yes","no")
    print(f"{player1_name}, pay attention now, cause this is where it gets serious..\n I chose - YOU to be the X-men.\n{player2_name}, you'll be the 0.")
    while True:
        game_tools = input("write down 'yes' to play!\n or 'no' to change that: ")
        if game_tools not in change_tools:
            print("what?")
        elif game_tools == "yes":
            players_tools.append("X")
            players_tools.append("O")
            return list
        else:
            players_tools.append("O")
            players_tools.append("X")
            return list


        #     tools_backward(x="O",o="X")
        # else: tools_forward(u="X",f="O")
#
# def tools_backward(*,x,o):
#     return (x,o)
#
# def tools_forward(*,u,f):
#     return (u,f)
amuda_X = []
amuda_O = []
shura_X = []
shura_O = []
def the_booth_list():
    for b in range(1,(board*board)+1):
        booth_list.append(b)
    for b in range(1, board + 1):
       amuda_X.append(0)
       amuda_O.append(0)
       shura_X.append(0)
       shura_O.append(0)

def tavla():
    space_no_end = "+~~~~~"
    space_end = "+"
    space = (f"{(space_no_end)*board}{space_end}")
    print(f" {space}")
    for i in range(0,(board*board),board):
        for j in range(1,board+1):
            booth = booth_list[((i+j)-1)]
            kir = "|"
            kirstart = (f" {kir}  {booth}")
            kirot1 = (f"  {booth}  ")
            kirot2 = (f" {booth}  ")
            kirot3 = (f" {booth} ")
            if type(booth) is int:
                if booth < 100:
                    if booth < 10:
                        if booth == 1:
                            print(kirstart,end="  |")
                        else: print(kirot1,end="|")
                    else: print(kirot2,end="|")
                else: print(kirot3, end="|")
            elif i==0 and j==1 and booth_list[0] == "X" or booth_list[0] == "O":
                print(kirstart, end="  |")
            else: print(kirot1,end="|")
        print('\n',space,'\n',end=" |")
    #game_is_on()

def game_is_on():
    print("ok, now pick a booth and make it yours. you can write down 'stop' anytime if you had enough")
    print(f"{player1_name} will start")
    while True:
        player1_turn()
        player2_turn()
def player1_turn():
    while True:
        #try:
            player1_booth = int(input(f"choose your booth Mr.{player1_name}"))
            if booth_list[player1_booth-1] != "X" or booth_list[player1_booth-1] != "O":
                booth_list[player1_booth-1] = players_tools[0]
                tavla()
                if checking_scores_alachsonim():
                    print(f"{player1_name} WON!!!")
                    playorquit()
                elif checking_scores_amudot():
                    print(f"{player1_name} WON!!!")
                    playorquit()
                elif checking_scores_shurot():
                    print(f"{player1_name} WON!!!")
                    playorquit()
                else:
                    break
            else:
                print("dont be a cheater")
        #except:
            #print("what1?")

def player2_turn():
    while True:
        #try:
            player2_booth = int(input(f"choose your booth Mr.{player2_name}"))
            if booth_list[player2_booth-1] != "X" or booth_list[player2_booth-1] != "O":
                booth_list[player2_booth-1] = players_tools[1]
                tavla()
                if checking_scores_alachsonim():
                    print(f"{player2_name} WON!!!")
                    playorquit()
                elif checking_scores_amudot():
                    print(f"{player2_name} WON!!!")
                    playorquit()
                elif checking_scores_shurot():
                    print(f"{player2_name} WON!!!")
                    playorquit()
                else:
                    break
            else:
                print("dont be a cheater")
        #except:
            #print("what2?")


def checking_scores_alachsonim():
    alachson_from_northwest_X = 0
    alachson_from_northwest_O = 0
    alachson_from_northeast_X = 0
    alachson_from_northeast_O = 0

    i = 0   # alachson from north-west \
    while i < board:
        if booth_list[((board * i) + i)] == "X":
            alachson_from_northwest_X += 1
        elif booth_list[((board * i) + i)] == "O":
            alachson_from_northwest_O += 1
        i += 1
    if alachson_from_northwest_X == board or alachson_from_northwest_O == board:
        return True
        # if alachson_from_northwest_X == board:
        #     print(f"{player1_name}...you won!!!!!!!")
        # else: print(f"{player2_name}...you won!!!!!!!")

    s = 0 # alachson from north-east /
    while s <= board:
        if booth_list[((board * s) - s)] == "X":
            alachson_from_northeast_X += 1
        elif booth_list[((board * s) - s)] == "O":
            alachson_from_northeast_O += 1
        s += 1
    if alachson_from_northeast_X == board or alachson_from_northeast_O == board:
        return True
    return False

def checking_scores_amudot():
    for val in range(0, 4):  # amudot |||
        c = -1
        while c < (board - 1):
            if booth_list[(board * c) + (val + board)] == "X":
                amuda_X[val] += 1
            elif booth_list[(board * c) + (val + board)] == "O":
                amuda_O[val] += 1
                # print(amuda_X)
                # print(amuda_X[val])
                # print(c)
                # print("---")
            if amuda_X[val] == board or amuda_O[val] == board:
                return True
            c += 1
            return False

def checking_scores_shurot():
    for dal in range(0, board):  # shurot ---
        e = -1
        while e < (board - 1):
            if booth_list[dal * board] == "X":
                shura_X[dal] += 1
            elif booth_list[(dal - board) + (e + 1)] == "O":
                shura_O[dal] += 1
                # print(amuda_X)
                # print(amuda_X[val])
                # print(c)
                # print("---")
            if shura_X[dal] == board or shura_O[dal] == board:
                return True
            e += 1
            return False
        # if alachson_from_northeast_X == board:
        #     print(f"{player1_name}...you won!!!!!!!")
        # else: print(f"{player2_name}...you won!!!!!!!")



#
# playersnames = player_names(player1_name,player2_name)

cmd = playorquit()
if cmd == "play":
    print("now just write down your Names cause that's super important of course..")
    player1_name = input("player 1 Name: ")
    player2_name = input("player 2 Name: ")
    tools()
    board = int(input("board's size: "))
    the_booth_list()
    tavla()
    game_is_on()
    #player_names(player1_name,player2_name)
else:
    print("bye bye")
    exit(0)

