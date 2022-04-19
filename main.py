# # #tictacto ⬜
from GameBoard import Board
from GamePlayer import Player

board = Board()
player_x = Player("x")
x_mark = player_x.mark
player_o = Player("o")
o_mark = player_o.mark
automatic_player = Player(" ")

def move(player, mark):
    user_input = player.set_input()
    board.convert_checkdouble_set_mark(user_input,mark)

def check_move(mark_1):
    if board.check_win(mark_1):
        print(f"{mark_1} wins")
        return True
    elif board.check_draw():
        print("oh, it's a draw")
        return True

print("Welcome to tictacto for terminal.\nWrite the number of the row and the letter of the column to set your (without spaces) to set your 'x' or 'o', when you are asked to.")

def start_game():
    game_on = True
    if automatic_player.set_automatic_player() == False:
        while game_on:
            move(player_x, x_mark)
            if check_move(x_mark):
                game_on = False
            else:
                move(player_o, o_mark)
                if check_move(o_mark):
                    game_on = False
    else:
        while game_on:
            if automatic_player.mark == "x":
                board.automatic_player_set_smart_move(automatic_player.mark)
                if check_move(automatic_player.mark):
                    game_on = False
                else:
                    move(player_o, o_mark)
                    if check_move(o_mark):
                        game_on = False
            else:
                move(player_x, x_mark)
                if check_move(x_mark):
                    game_on = False
                else:
                    board.automatic_player_set_smart_move(automatic_player.mark)
                    if check_move(automatic_player.mark):
                        game_on = False

    again_q = input("Do you want to play another round of TictacTo? y or n: ")
    if again_q == "y":
        board.reset_attributes()
        start_game()
    else:
        print("ByeBye")

start_game()





