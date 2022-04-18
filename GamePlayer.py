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
                return True
            else:
                self.mark = "x"
                return True
        else:
            return False

    def set_input(self):
        player_input = input("Decide: ").lower()
        pattern = re.compile(r"[1-3][a|b|c]$")
        match = pattern.match(player_input)
        while match == None:
            player_input = input("Please type in first the nuber of the row and afterward the letter of the column without spaces: ").lower()
            match = pattern.match(player_input)
        return player_input

