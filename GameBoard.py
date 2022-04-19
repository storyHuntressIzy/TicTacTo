from random import choice

class Board:
    def __init__(self):
        self.head_list = ["___A___B___C__"]
        self.break_list = ["--------------"]
        self.row_1 = ["1| ", " ", " | ", " ", " | ", " ", " |"]
        self.row_2 = ["2| ", " ", " | ", " ", " | ", " ", " |"]
        self.row_3 = ["3| ", " ", " | ", " ", " | ", " ", " |"]
        self.map = [self.head_list, self.row_1, self.row_2, self.row_3]
        self.col = 0
        self.row = 0
        self.all_marks = [[1,1],[1,3],[1,5],[2,1],[2,3],[2,5],[3,1],[3,3],[3,5]]
    
    def print_map(self):
        print(f"{''.join(self.head_list)}\n{''.join(self.row_1)}\n{''.join(self.break_list)}\n{''.join(self.row_2)}\n{''.join(self.break_list)}\n{''.join(self.row_3)}")

    def reset_col_and_row(self):
        self.col = 0
        self.row = 0

    def convert_checkdouble_set_mark(self, player_input, player_mark):
        y = [char for char in player_input][0]
        self.row += int(y)
        x = [char for char in player_input][1]
        if x == "a":
            self.col += 1
        elif x == "b":
            self.col += 3
        elif x == "c":
            self.col += 5
        while self.map[self.row][self.col] == "x" or self.map[self.row][self.col] == "o":
            self.reset_col_and_row()
            new_input = input("Do not try to cheat! This spot is already taken. Type in a new mark: ")
            x = [char for char in new_input][1]
            if x == "a":
                self.col += 1
            elif x == "b":
                self.col += 3
            elif x == "c":
                self.col += 5
            y = [char for char in new_input][0]
            self.row += int(y)
        self.map[self.row][self.col] = player_mark
        self.all_marks = [mark_list for mark_list in self.all_marks if mark_list != [self.row, self.col]]
        self.reset_col_and_row()
        self.print_map()

    def check_win(self, xoro):
        for i in range(1,4):
            if self.map[i][1] == xoro and self.map[i][3] == xoro and self.map[i][5] == xoro:
                return True
        for i in range(1,6,2):
            if self.map[1][i] == xoro and self.map [2][i] == xoro and self.map[3][i] == xoro:
                return True
        if self.map[1][1] == xoro and self.map[2][3] == xoro and self.map[3][5] == xoro:
            return True
        if self.map[1][5] == xoro and self.map[2][3] == xoro and self.map[3][1] == xoro:
            return True
    
    def automatic_player_set_smart_move(self, xoro):
        win = True
        impede_win = False
        if xoro == "x":
            other = "o"
        elif xoro == "o":
            other = "x"
        if win == True:
            for mark in self.all_marks:
                self.row = mark[0]
                self.col = mark[1]
                self.map[self.row][self.col] = xoro
                if self.check_win(xoro) == True:
                    self.print_map()
                    break
                else:
                    self.map[self.row][self.col] = " "
                    win = False
                    impede_win = True
        if impede_win == True:
            for mark in self.all_marks:
                self.row = mark[0]
                self.col = mark[1]
                self.map[self.row][self.col] = other
                if self.check_win(other) == True:
                    self.map[self.row][self.col] = xoro
                    self.all_marks = [mark_list for mark_list in self.all_marks if mark_list != [self.row, self.col]]
                    self.print_map()
                    self.reset_col_and_row()
                    impede_win = True
                    break
                else:
                    self.map[self.row][self.col] = " "
                    self.reset_col_and_row()
                    impede_win = False
        if win == False and impede_win == False:
            random_mark = choice(self.all_marks)
            self.col = random_mark[1]
            self.row = random_mark[0]
            self.map[self.row][self.col] = xoro
            self.all_marks = [mark_list for mark_list in self.all_marks if mark_list != [self.row, self.col]]
            self.reset_col_and_row()
            self.print_map()


    def check_draw(self):
        draw = 0
        for i in range(1,4):
            if self.map[i][1] != " " and self.map[i][3] != " " and self.map[i][5] != " ":
                draw += 1
            if draw == 3:
                return True


    def reset_attributes(self):
        self.all_marks = [[1,1],[1,2],[1,3],[1,5],[2,1],[2,3],[2,5],[3,1],[3,3],[3,5]]
        for mark in self.all_marks:
            self.row = mark[0]
            self.col = mark[1]
            self.map[self.row][self.col] = " "
        self.col = 0
        self.row = 0

