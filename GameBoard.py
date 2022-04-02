class Board:
    def __init__(self):
        self.head_list = ["___A___B___C__"]
        self.break_list = ["--------------"]
        self.row_1 = ["1| ", " ", " | ", " ", " | ", " ", " |"]
        self.row_2 = ["2| ", " ", " | ", " ", " | ", " ", " |"]
        self.row_3 = ["3| ", " ", " | ", " ", " | ", " ", " |"]
        self.map = [self.head_list, self.row_1, self.row_2, self.row_3]
        self.mapshow = f"{''.join(self.head_list)}\n{''.join(self.row_1)}\n{''.join(self.break_list)}\n{''.join(self.row_2)}\n{''.join(self.break_list)}\n{''.join(self.row_3)}"
        self.col = 0
        self.row = 0
    
    
    def set_mark(self, player_input, player_mark):
        x = [char for char in player_input][1]
        if x == "a":
            self.col += 1
        elif x == "b":
            self.col += 3
        elif x == "c":
            self.col += 5
        y = [char for char in player_input][0]
        self.row += int(y)
        if self.map[self.row][self.col] == "x" or self.map[self.row][self.col] == "o":
            self.col = 0
            self.row = 0
            return False
        else:
            self.map[self.row][self.col] = player_mark
            self.col = 0
            self.row = 0
            print(f"{''.join(self.head_list)}\n{''.join(self.row_1)}\n{''.join(self.break_list)}\n{''.join(self.row_2)}\n{''.join(self.break_list)}\n{''.join(self.row_3)}")

    def check_win_x(self):
        for i in range(1,4):
            if self.map[i][1] == "x" and self.map[i][3] == "x" and self.map[i][5] == "x":
                return True
        for i in range(1,6,2):
            if self.map[1][i] == "x" and self.map [2][i] == "x" and self.map[3][i] == "x":
                return True
        if self.map[1][1] == "x" and self.map[2][3] == "x" and self.map[3][5] == "x":
            return True
        if self.map[1][5] == "x" and self.map[2][3] == "x" and self.map[3][1] == "x":
            return True
    
    def check_win_o(self):
        for i in range(1,4):
            if self.map[i][1] == "o" and self.map[i][3] == "o" and self.map[i][5] == "o":
                return True
        for i in range(1,6,2):
            if self.map[1][i] == "o" and self.map [2][i] == "o" and self.map[3][i] == "o":
                return True
        if self.map[1][1] == "o" and self.map[2][3] == "o" and self.map[3][5] == "o":
            return True
        if self.map[1][5] == "o" and self.map[2][3] == "o" and self.map[3][1] == "o":
            return True
    
    def check_draw(self):
        draw = 0
        for i in range(1,4):
            if self.map[i][1] != " " and self.map[i][3] != " " and self.map[i][5] != " ":
                draw += 1
            if draw == 3:
                return True

    def reset_board(self):
        self.row_1 = ["1| ", " ", " | ", " ", " | ", " ", " |"]
        self.row_2 = ["2| ", " ", " | ", " ", " | ", " ", " |"]
        self.row_3 = ["3| ", " ", " | ", " ", " | ", " ", " |"]
    
    #Liste ausgeben mit freien positionen die ich an gameplayer zurückgeben kann 

    #pc spieler soll immer chekcnen obs ne freie position gibt mit der er theoretishch gewinnen kann (check_win_x or check_win_o)

    #while loops in ne funtion zu machen, aber die while loop darf in der funktion bleiben 