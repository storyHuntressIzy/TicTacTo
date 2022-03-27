# # #tictacto ⬜
from GameBoard import Board
from GamePlayer import Player

board = Board()
player_x = Player("x")
x_mark = player_x.mark
player_o = Player("o")
o_mark = player_o.mark
game_on = True
pc_x = False
pc_o = False

print("Welcome to tictacto for terminal.") 
print(board.mapshow)

def start_game():
    alone_q = input("Are you playing alone? y or n: ")
    if alone_q == "y":
        x_or_o = input("Do want to play first or second?: ").lower()
        if x_or_o == "first":
            pc_o = True
        else:
            pc_x = True

    print("Write the number of the row and the letter of the column to set your (without spaces) to set your 'x' or 'o', when you are asked to.")


    while game_on:
        if pc_x == True:
            x_input = player_x.pc_player()
        else:
            x_input = input("Decide x: ")
        while player_x.check_input(x_input) == False:
            x_input = input("Please type in your answer correctly: ").lower()
        while board.set_mark(x_input, x_mark) == False:
            if pc_x == True:
                x_input = player_x.pc_player()
            else:
                x_input = input("This spot is taken. Please set another mark: ").lower()
        if board.check_win_x() == True:
            print("x wins!")
            game_on = False
        elif board.check_draw() == True:
            print("It's a draw")
            game_on = False
        else:
            if pc_o == True:
                o_input = player_o.pc_player()
            else:
                o_input = input("Decide o: ").lower()
            while player_o.check_input(o_input) == False:
                o_input = input("Please type in your answer correctly: ").lower()
            while board.set_mark(o_input, o_mark) == False:
                if pc_o == True:
                    o_input = player_o.pc_player()
                else:
                    o_input = input("This spot is taken. Please set another mark: ").lower()
            if board.check_win_o() == True:
                print("o wins!")
                game_on = False
            elif board.check_draw() == True:
                print("It's a draw")
                game_on = False

again_q = input("Do you want to play another round of TictacTo? y or n: ")
if again_q == "y":
    board.reset_board()
else:
    print("ByeBye")





