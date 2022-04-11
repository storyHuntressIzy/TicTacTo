import random

class Player:
    def __init__(self,xoro):
        self.mark = xoro
        self.automatic_player_x = False
        self.automatic_player_o = False
    

    def set_automatic_player(self):
        alone_q = input("Are you playing alone? y or n: ")
        if alone_q == "y":
            x_or_o = input("Do want to play first or second?: ").lower()
            if x_or_o == "first":
                self.mark = "o"
                self.automatic_player_o = True
            else:
                self.mark = "x"
                self.automatic_player_x = True


    def set_input(self):
        if self.automatic_player_o == True or self.automatic_player_x == True:
            pass
        else:
            player_input = input("Decide: ")
            check_list = [char for char in player_input]
            while (check_list[0] not in ["1", "2", "3"]) or (check_list[1] not in ["a", "b", "c"]) or (len(check_list) > 2):
                new_input = input("Please type in first the nuber of the row and afterward the letter of the column without spaces: ").lower()
                check_list = [char for char in new_input]
                return new_input
            return player_input
        

    # get_pc_player_move
    # def pc_player(self):
    #     row = ["1", "2", "3"]
    #     col = ["a", "b", "c"]
    #     mark = random.choice(row) + random.choice(col)
    #     return mark
