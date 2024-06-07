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

def main():
    # User input for Sudoku puzzle ('b' denotes empty cells)
    board = []
    print("Enter the Sudoku puzzle row by row (use 'b' for empty cells):")
    for i in range(9):
        row_input = input(f"Row {i + 1}: ").strip()
        if len(row_input) != 9 or not all(c.isdigit() or c == 'b' for c in row_input):
            print("Invalid input. Each row must contain exactly 9 characters, either digits or 'b'.")
            return
        row = [int(c) if c != 'b' else 0 for c in row_input]
        board.append(row)

    print("\nSudoku puzzle to solve:")
    print_board(board)

    if solve_sudoku(board):
        print("Solved Sudoku puzzle:")
        print_board(board)
    else:
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()
