# Mendi Lirmak 316162510
# Dana Farber 209376359
# Shoval Omesi 307984294

from solver import Solver
class Board:
    def __init__(self):
        self.board = [
            [4, 6, ' ', 2, ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 1, 6, 9, ' ', ' ', ' ', ' '],
            [' ', 7, 8, ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 4, ' ', 8, ' ', ' ', ' ', 1],
            [9, ' ', ' ', ' ', ' ', ' ', ' ', ' ', 7],
            [7, ' ', ' ', ' ', 4, ' ', 3, ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 6, 8, ' '],
            [' ', ' ', ' ', ' ', 5, 9, 2, ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 6, ' ', 9, 3]
        ]
        self.changed_cells = Solver.solve_board(self.board)
        self.sub_grid_print=False

    def place_cards_according_to_step1(self):
        for row in range(9):
            for col in range(9):
                cell_value = self.board[row][col]
                self.board[row][col] = [cell_value, cell_value, cell_value]


    def print_solved_board_with_hidden_cards(self):
        horizontal_line = "+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------"
        print(horizontal_line)
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print("|-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------|")
            row_str = "| "
            for j, cell in enumerate(row):
                if not self.sub_grid_print:
                    if (i, j, cell[0]) in self.changed_cells:
                        dynamic_string = "["
                        for _ in range(len(cell)):
                            dynamic_string += "?"
                            if _ != len(cell) - 1:
                                dynamic_string += ", "
                        dynamic_string += "] "
                        row_str += dynamic_string
                    else:
                        row_str += str(cell) + " "
                else:
                    if (i, j, cell) in self.changed_cells:
                        dynamic_string = "["
                        for _ in range(len(cell)):
                            dynamic_string += "?"
                            if _ != len(cell) - 1:
                                dynamic_string += ", "
                        dynamic_string += "] "
                        row_str += dynamic_string
                    else:
                        row_str += str(cell) + " "
                if (j + 1) % 3 == 0:
                    row_str += "| "
            print(row_str)
        print(horizontal_line)