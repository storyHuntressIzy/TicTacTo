# # #tictacto ⬜
from GameBoard import Board
from GamePlayer import Player

print("Welcome to tictacto for terminal.") 

board = Board()
player_x = Player("x")
x_mark = player_x.mark
player_o = Player("o")
o_mark = player_o.mark
automatic_player = Player(" ")
automatic_player.set_automatic_player()
game_on = True

print("Write the number of the row and the letter of the column to set your (without spaces) to set your 'x' or 'o', when you are asked to.")

print(board.mapshow)
 
input_x = player_x.set_input()
print(input_x)

# while game_on:
#     input_x = input("Decide: ")
#     player_x.check_input(input_x)
#     converted_x_mark = board.convert_mark(input_x)
#     board.check_double_mark()
#     board.set_mark(x_mark, converted_x_mark)
#     if board.check_win(x_mark):
#         print("x wins!")
#         game_on = False
#     elif board.check_draw():
#         print("oh, its a draw!")
#         game_on = False
#     else:
#         input_o = input("Decide: ")
#         player_o.check_input(input_o)
#         converted_o_mark = board.convert_mark(input_o)
#         board.check_double_mark()
#         board.set_mark(o_mark, converted_o_mark)
#         if board.check_win(o_mark):
#             print("o wins!")
#             game_on = False
#         elif board.check_draw():
#             print("oh, it's a draw")
#             game_on = False

# again_q = input("Do you want to play another round of TictacTo? y or n: ")
# if again_q == "y":
#     board.reset_board_and_mark_lists()
# else:
#     print("ByeBye")
