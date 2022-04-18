# # #tictacto ⬜
from GameBoard import Board
from GamePlayer import Player

def play_alone():
    game_on = True
    board.reset_attributes()
    while game_on:
        automatic_mark = automatic_player.mark
        if automatic_mark == "x":
            board.automatic_player_set_smart_move(automatic_mark)
            if board.check_win(automatic_mark) == True:
                print("AP wins")
                game_on = False
            elif board.check_draw():
                game_on = False
            else:
                o_input = player_o.set_input()
                board.convert_checkdouble_set_mark(o_input, o_mark)
                if board.check_win(o_mark):
                    print("o wins!")
                    game_on = False
                elif board.check_draw():
                    print("oh, it's a draw")
                    game_on = False
        
        if automatic_mark == "o":
            print(automatic_mark)
            input_x = player_x.set_input()
            board.convert_checkdouble_set_mark(input_x, x_mark)
            if board.check_win(x_mark):
                print("x wins")
                game_on = False
            elif board.check_draw():
                print("oh it's a draw")
                game_on = False
            else:
                board.automatic_player_set_smart_move(automatic_mark)
                if board.check_win(automatic_mark) == True:
                    print("AP wins")
                    game_on = False
                elif board.check_draw():
                    print("Oh it's a draw")

def play_together():
    game_on = True
    while game_on == True:
        input_x = player_x.set_input()
        board.convert_checkdouble_set_mark(input_x, x_mark)
        if board.check_win(x_mark):
            print("x wins!")
            game_on = False
        elif board.check_draw():
            print("oh, its a draw!")
            game_on = False
        else:
            input_o = player_o.set_input()
            board.convert_checkdouble_set_mark(input_o, o_mark)
            if board.check_win(o_mark):
                print("o wins!")
                game_on = False
            elif board.check_draw():
                print("oh, it's a draw")
                game_on = False

def start_and_end_game():
    if automatic_player.set_automatic_player() == False:
        play_together()
    else:
        play_alone()
    again_q = input("Do you want to play another round of TictacTo? y or n: ")
    if again_q == "y":
        start_and_end_game()
    else:
        print("ByeBye")

board = Board()
player_x = Player("x")
x_mark = player_x.mark
player_o = Player("o")
o_mark = player_o.mark
automatic_player = Player(" ")


print("Welcome to tictacto for terminal.") 
print("Write the number of the row and the letter of the column to set your (without spaces) to set your 'x' or 'o', when you are asked to.")

start_and_end_game()