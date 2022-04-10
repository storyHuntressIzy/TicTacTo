import random

class Player:
    def __init__(self,xoro):
        self.mark = xoro
    
    # denk dir was aus, die schon belegten felder aus der random ding rausnimmt. 
    # get_pc_player_move
    def pc_player(self):
        row = ["1", "2", "3"]
        col = ["a", "b", "c"]
        mark = random.choice(row) + random.choice(col)
        return mark

    def check_input(self, player_input):
        check_list = [char for char in player_input]
        while (check_list[0] not in ["1", "2", "3"]) or (check_list[1] not in ["a", "b", "c"]) or (len(check_list) > 2):
            new_input = input("Please type in first the nuber of the row and afterward the letter of the column without spaces: ").lower()
            check_list = [char for char in new_input]
