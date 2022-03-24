class Board:
    def __init__(self):
        head_list = ["___A___B___C__"]
        break_list = ["--------------"]
        row_1 = ["1| ", " ", " | ", " ", " | ", " ", " |"]
        row_2 = ["2| ", " ", " | ", " ", " | ", " ", " |"]
        row_3 = ["3| ", " ", " | ", " ", " | ", " ", " |"]
        self.map = [head_list, row_1, row_2, row_3]
        self.mapshow = f"{''.join(head_list)}\n{''.join(row_1)}\n{''.join(break_list)}\n{''.join(row_2)}\n{''.join(break_list)}\n{''.join(row_3)}"
    

    