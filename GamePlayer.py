import re

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
            player_input = input("Decide: ").lower()
            pattern = re.compile(r"[a|b|c][1-3]")
            match = pattern.match(player_input)
            print(match)
            while match == None or len(player_input) > 2:
                player_input = input("Please type in first the nuber of the row and afterward the letter of the column without spaces: ").lower()
                match = pattern.match(player_input)
            return player_input

    # warum funktionier ,{2} in re nicht anstelle von len