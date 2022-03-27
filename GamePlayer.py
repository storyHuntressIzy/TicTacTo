import random

class Player:
    def __init__(self,xoro):
        self.mark = xoro
    

    def pc_player(self):
        row = ["1", "2", "3"]
        col = ["a", "b", "c"]
        mark = random.choice(row) + random.choice(col)
        return mark

    def check_input(self, player_input):
        passed = False
        check_list = [char for char in player_input]
        if check_list[0] == "1" or check_list[0] =="2" or check_list[0] == "3": 
            passed = True
        if check_list[1] == "a" or check_list[1] == "b" or check_list[1] == "c":
            passed = True
        if len(check_list) > 2:
            passed = False
        return passed
    
