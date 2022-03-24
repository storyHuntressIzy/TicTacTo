# # #tictacto ⬜
import random
from GameBoard import Board

def split(order):
    return [char for char in order]

def set_col(player_input):
    x = split(player_input)[1]
    if x == "a":
        return 1
    elif x == "b":
        return 3
    elif x == "c":
        return 5

def set_row(player_input):
    x = split(player_input)[0]
    return int(x)

def check_x(map):
    for i in range(1,4):
        if map[i][1] == "x" and map[i][3] == "x" and map[i][5] == "x":
            return False
    for i in range(1,6,2):
        if map[1][i] == "x" and map [2][i] == "x" and map[3][i] == "x":
            return False
    if map[1][1] == "x" and map[2][3] == "x" and map[3][5] == "x":
        return False
    if map[1][5] == "x" and map[2][3] == "x" and map[3][1] == "x":
        return False


def check_o(map):
    for i in range(1,4):
        if map[i][1] == "o" and map[i][3] == "o" and map[i][5] == "o":
            return False
    for i in range(1,6,2):
        if map[1][i] == "o" and map [2][i] == "o" and map[3][i] == "o":
            return False
    if map[1][1] == "o" and map[2][3] == "o" and map[3][5] == "o":
        return False
    if map[1][5] == "o" and map[2][3] == "o" and map[3][1] == "o":
        return False

def check_draw(map):
    draw = 0
    for i in range(1,4):
        if map[i][1] != " " and map[i][3] != " " and map[i][5] != " ":
            draw += 1
        if draw == 3:
            return False

def player():
    row = ["1", "2", "3"]
    col = ["a", "b", "c"]
    mark = random.choice(row) + random.choice(col)
    return mark

def start():
    head_list = ["___A___B___C__"]
    break_list = ["--------------"]
    row_1 = ["1| ", " ", " | ", " ", " | ", " ", " |"]
    row_2 = ["2| ", " ", " | ", " ", " | ", " ", " |"]
    row_3 = ["3| ", " ", " | ", " ", " | ", " ", " |"]
    map = [head_list, row_1, row_2, row_3]
    game_on= True
    pc_player_x = False
    pc_player_o = False

    alone_q = input("Are you playing alone? y or n: ")
    if alone_q == "y":
        x_or_o = input("Do want to play first or second?: ").lower()
        if x_or_o == "first":
            pc_player_o = True
        else:
            pc_player_x = True


    print("Write the number of the row and the letter of the column to set your (without spaces) to set your 'x' or 'o', when you are asked to.")
    print(f"{''.join(head_list)}\n{''.join(row_1)}\n{''.join(break_list)}\n{''.join(row_2)}\n{''.join(break_list)}\n{''.join(row_3)}")

    while game_on:

        if pc_player_x == True:
            player_x = player()
        else:
            player_x = input("Where do you want to mark your 'x'? ").lower()
        col_x = set_col(player_x)
        row_x = set_row(player_x)
        while map[row_x][col_x] != " ":
            if pc_player_x == True:
                player_x = player()
            else:
                player_x = input("Please do not try to cheat. This spot is already marked. Please enter your mark of choice again: ")
            col_x = set_col(player_x)
            row_x = set_row(player_x)
        map[row_x][col_x] = "x"
        print(f"{''.join(head_list)}\n{''.join(row_1)}\n{''.join(break_list)}\n{''.join(row_2)}\n{''.join(break_list)}\n{''.join(row_3)}")
        if check_x(map) == False:
            print("x wins")
            game_on = False
        elif check_draw(map) == False:
            print("It's a draw")
            game_on = False
        else:
            if pc_player_o == True:
                player_o = player()
            else:
                player_o = input("Where do you want to mark your 'o'? ").lower()
            col_o = set_col(player_o)
            row_o = set_row(player_o)
            while map[row_o][col_o] != " ":
                if pc_player_o == True:
                    player_o = player()
                else:
                    player_o = input("Please do not try to cheat. This spot is already marked. Please enter your mark of choice again: ")
                col_o = set_col(player_o)
                row_o = set_row(player_o)
            map[row_o][col_o] = "o"
            print(f"{''.join(head_list)}\n{''.join(row_1)}\n{''.join(break_list)}\n{''.join(row_2)}\n{''.join(break_list)}\n{''.join(row_3)}")
            if check_o(map) == False:
                print("o wins")
                game_on = False
            elif check_draw(map) == False:
                print("It's a draw")
                game_on = False
    
    again_q = input("Wanna play again? y or n: ")
    if again_q == "y":
        row_1 = ["1| ", " ", " | ", " ", " | ", " ", " |"]
        row_2 = ["2| ", " ", " | ", " ", " | ", " ", " |"]
        row_3 = ["3| ", " ", " | ", " ", " | ", " ", " |"]
        start()
    else:
        print("ByeBye")

# print("Welcome to tictacto for terminal.") 

# start()

board = Board()
