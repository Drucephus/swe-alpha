def print_board(board):
    """Helper function to print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()

def find_empty_location(board):
    """Find an empty location on the board (denoted by 0)."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    """Check if placing the number at the position is valid."""
    row, col = pos

    # Check the row
    for j in range(len(board[0])):
        if board[row][j] == num and col != j:
            return False

    # Check the column
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    # Check the 3x3 subgrid
    subgrid_x = row // 3
    subgrid_y = col // 3
    for i in range(subgrid_x * 3, subgrid_x * 3 + 3):
        for j in range(subgrid_y * 3, subgrid_y * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty_location = find_empty_location(board)
    if not empty_location:
        return True  # Puzzle solved
    else:
        row, col = empty_location

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack

    return False

def is_valid_row(board, row):
    """Check if the row is valid according to Sudoku rules."""
    row_set = set()
    for num in board[row]:
        if num != 0:
            if num in row_set:
                return False
            row_set.add(num)
    return True

def is_valid_column(board, col, up_to_row):
    """Check if the column is valid according to Sudoku rules up to a specific row."""
    col_set = set()
    for i in range(up_to_row + 1):
        if board[i][col] != 0:
            if board[i][col] in col_set:
                return False
            col_set.add(board[i][col])
    return True

def is_valid_subgrid(board, row, col):
    """Check if the 3x3 subgrid is valid according to Sudoku rules."""
    subgrid_set = set()
    subgrid_x = row // 3
    subgrid_y = col // 3
    for i in range(subgrid_x * 3, subgrid_x * 3 + 3):
        for j in range(subgrid_y * 3, subgrid_y * 3 + 3):
            if i < len(board) and j < len(board[i]) and board[i][j] != 0:
                if board[i][j] in subgrid_set:
                    return False
                subgrid_set.add(board[i][j])
    return True

def is_valid_board_incremental(board, row):
    """Check if the board is valid incrementally."""
    # Check the current row
    if not is_valid_row(board, row):
        return False

    # Check all columns up to the current row
    for col in range(9):
        if not is_valid_column(board, col, row):
            return False

    # Check all subgrids up to the current row
    for subgrid_x in range((row // 3) + 1):
        for subgrid_y in range(3):
            if not is_valid_subgrid(board, subgrid_x * 3, subgrid_y * 3):
                return False

    return True

def main():
    # User input for Sudoku puzzle ('.' denotes empty cells)
    board = []
    print("Enter the Sudoku puzzle row by row (use '.' for empty cells):")
    for i in range(9):
        while True:
            row_input = input(f"Row {i + 1}: ").strip()
            if len(row_input) != 9 or not all(c.isdigit() or c == '.' for c in row_input):
                print("Invalid input. Each row must contain exactly 9 characters, either digits or '.'. Please re-enter the row.")
                continue
            row = [int(c) if c != '.' else 0 for c in row_input]
            board.append(row)
            if not is_valid_board_incremental(board, i):
                print("Invalid input. The row violates Sudoku rules. Please re-enter the row.")
                board.pop()
            else:
                break

    print("\nSudoku puzzle to solve:")
    print_board(board)

    if solve_sudoku(board):
        print("Solved Sudoku puzzle:")
        print_board(board)
    else:
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()

