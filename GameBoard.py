from random import choice

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
        self.all_marks = [[1,1],[1,2],[1,3],[1,5],[2,1],[2,3],[2,5],[3,1],[3,3],[3,5]]
        self.x_marks = []
        self.o_marks = []
    
    
    def convert_mark(self, player_input):
        x = [char for char in player_input][1]
        if x == "a":
            self.col += 1
        elif x == "b":
            self.col += 3
        elif x == "c":
            self.col += 5
        y = [char for char in player_input][0]
        self.row += int(y)
        converted_mark = [self.row, self.col]
        return converted_mark

    def check_double_mark(self):
        while self.map[self.row][self.col] == "x" or self.map[self.row][self.col] == "o":
            self.col = 0
            self.row = 0
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
            

    def set_mark(self, player_mark, converted_mark):
        self.row = converted_mark[0]
        self.col = converted_mark[1]
        self.map[self.row][self.col] = player_mark
        if player_mark == "x":
            self.x_marks.append([self.row, self.col])
        else:
            self.o_marks.append([self.row, self.col])
        self.all_marks = [mark_list for mark_list in self.all_marks if mark_list != [self.col, self.row]]
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

    def automatic_player_checks_win(self, xoro):
        for i in range(1,4):
            if self.map[i][1] == " " and self.map[i][3] == xoro and self.map[i][5] == xoro:
                mark = [i,1]
                return mark
            elif self.map[i][1] == xoro and self.map[i][3] == " " and self.map[i][5] == xoro:
                mark = [i,3]
                return mark
            elif self.map[i][1] == xoro and self.map[i][3] == xoro and self.map[i][5] == " ":
                mark = [i,5]
                return mark

    def automatic_player_checks_win_col(self, xoro): 
        for i in range(1,6,2):
            if self.map[1][i] == " " and self.map[2][i] == xoro and self.map[3][i] == xoro:
                mark = [1,i]
                return mark
            elif self.map[1][i] == xoro and self.map[2][i] == " " and self.map[3][i] == xoro:
                mark = [2,i]
                return mark
            elif self.map[1][i] == xoro and self.map[2][i] == xoro and self.map[3][i] == " ":
                mark = [2,i]
                return mark
    
    def automatic_player_checks_win_diagonally(self, xoro):
        if self.map[1][1] == " " and self.map[2][3] == xoro and self.map[3][5] == xoro:
            mark = [1, 1]
            return mark
        elif self.map[1][1] == xoro and self.map[2][3] == " " and self.map[3][5] == xoro:
            mark = [2,3]
            return mark
        elif self.map[1][1] == xoro and self.map[2][3] == xoro and self.map[3][5] == " ":
            mark = [3,5]
            return mark

        elif self.map[1][5] == " " and self.map[2][3] == xoro and self.map[3][1] == xoro:
            mark = [1,5]
            return mark
        elif self.map[1][5] == xoro and self.map[2][3] == " " and self.map[3][1] == xoro:
            mark = [2,3]
            return mark
        elif self.map[1][5] == xoro and self.map[2][3] == xoro and self.map[3][1] == " ":
            mark = [3,1]
            return mark
        else:
            random_mark = choice(self.all_marks)
            self.col = random_mark[0]
            self.row = random_mark[1]
            self.map[self.col][self.row] = xoro



    def reset_board_and_mark_lists(self):
        self.row_1 = ["1| ", " ", " | ", " ", " | ", " ", " |"]
        self.row_2 = ["2| ", " ", " | ", " ", " | ", " ", " |"]
        self.row_3 = ["3| ", " ", " | ", " ", " | ", " ", " |"]
        self.all_marks = [[1,1],[1,2],[1,3],[1,5],[2,1],[2,3],[2,5],[3,1],[3,3],[3,5]]
        self.x_marks = []
        self.o_marks = []

    #pc spieler soll immer chekcnen obs ne freie position gibt mit der er theoretishch gewinnen kann (check_win_x or check_win_o)

    def show_free_position(self):
        position_list = [[]]
        return print(position_list)