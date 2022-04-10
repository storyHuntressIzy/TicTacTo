# # #tictacto ⬜
from GameBoard import Board
from GamePlayer import Player

print("Welcome to tictacto for terminal.") 

def start_game():
    board = Board()
    player_x = Player("x")
    x_mark = player_x.mark
    player_o = Player("o")
    o_mark = player_o.mark
    game_on = True
    pc_x = False
    pc_o = False
    print(board.mapshow)
    alone_q = input("Are you playing alone? y or n: ")
    if alone_q == "y":
        x_or_o = input("Do want to play first or second?: ").lower()
        if x_or_o == "first":
            pc_o = True
        else:
            pc_x = True

#start_game()

board = Board()
player_x = Player("x")
x_mark = player_x.mark
player_o = Player("o")
o_mark = player_o.mark
game_on = True
pc_x = False
pc_o = False

print("Write the number of the row and the letter of the column to set your (without spaces) to set your 'x' or 'o', when you are asked to.")

print(board.mapshow)

while game_on:
    input_x = input("Decide: ")
    player_x.check_input(input_x)
    converted_x_mark = board.convert_mark(input_x)
    board.check_double_mark()
    board.set_mark(x_mark, converted_x_mark)
    if board.check_win_x():
        print("x wins!")
        game_on = False
    elif board.check_draw():
        print("oh, its a draw!")
        game_on = False
    else:
        input_o = input("Decide: ")
        player_o.check_input(input_o)
        converted_o_mark = board.convert_mark(input_o)
        board.check_double_mark()
        board.set_mark(o_mark, converted_o_mark)
        if board.check_win_o():
            print("o wins!")
            game_on = False
        elif board.check_draw():
            print("oh, it's a draw")
            game_on = False

again_q = input("Do you want to play another round of TictacTo? y or n: ")
if again_q == "y":
    board.reset_board_and_mark_lists()
    start_game()
else:
    print("ByeBye")
