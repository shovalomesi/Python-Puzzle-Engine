# Mendi Lirmak 316162510
# Dana Farber 209376359
# Shoval Omesi 307984294

class Solver:
    def solve_board(board):
        changed_cells = []

        def is_valid_placement(row, col, num):
            if num in board[row]:
                return False
            
            if num in [board[i][col] for i in range(9)]: 
                return False

            subgrid_row_start = (row // 3) * 3
            subgrid_col_start = (col // 3) * 3
            for i in range(subgrid_row_start, subgrid_row_start + 3):
                for j in range(subgrid_col_start, subgrid_col_start + 3):
                    if board[i][j] == num:
                        return False
            
            return True

        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == " ":
                        for num in range(1, 10):
                            if is_valid_placement(row, col, num):
                                board[row][col] = num
                                changed_cells.append((row, col, num))
                                if solve():
                                    return True
                                board[row][col] = " "
                                changed_cells.pop()
                        return False
            return True

        solve()
        return changed_cells